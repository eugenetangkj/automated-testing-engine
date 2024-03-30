# Test Report

Time: 2024-03-30 08:56:14.160096

### Base Program

```py
def subsetXORSum(nums):
    ans = 0
    n = len(nums)
    max_val = 1 << n
    for i in range(1, max_val):
        xor_total = 0
        for j in range(n):
            if i & (1 << j):
                xor_total ^= nums[j]
        ans += xor_total
    return ans
```

## Test Case 1

### Modified Program

```py
def subsetXORSum(nums):
    ans = 0
    n = len(nums)
    max_val = 1 << n
    for i in range(1, max_val):
        xor_total = 0
        for j in range(n):
            if i & 1 << j:
                xor_total ^= nums[j]
        ans += xor_total
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def subsetXORSum(nums):\n    ans = 0\n    n = len(nums)\n    max_val = 1 << n\n    for i in range(1, max_val):\n        xor_total = 0\n        for j in range(n):\n            if i & 1 << j:\n                xor_total ^= nums[j]\n        ans += xor_total\n    return ans"
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
        "subsetXORSum": {
            "name": "subsetXORSum",
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
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "nums",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "max_val",
                        "val1": {
                            "name": "LShift",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
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
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "max_val",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
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
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
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
                            "i",
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
                            "i",
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
                        "val0": "xor_total",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "xor_total",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                        "val0": "xor_total",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "LShift",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 8,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_total",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                "1": "around the beginning of function 'subsetXORSum'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "xor_total": "*",
                "max_val": "*",
                "ind#1": "int",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*",
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
def subsetXORSum(var_0):
    ans = 0
    n = len(var_0)
    max_val = 1 << n
    for i in range(1, max_val):
        xor_total = 0
        for j in range(n):
            if i & 1 << j:
                xor_total ^= var_0[j]
        ans += xor_total
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def subsetXORSum(var_0):\n    ans = 0\n    n = len(var_0)\n    max_val = 1 << n\n    for i in range(1, max_val):\n        xor_total = 0\n        for j in range(n):\n            if i & 1 << j:\n                xor_total ^= var_0[j]\n        ans += xor_total\n    return ans"
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
        "subsetXORSum": {
            "name": "subsetXORSum",
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
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "max_val",
                        "val1": {
                            "name": "LShift",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
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
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "max_val",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
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
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
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
                            "i",
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
                            "i",
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
                        "val0": "xor_total",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "xor_total",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                        "val0": "xor_total",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "LShift",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 8,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_total",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                "1": "around the beginning of function 'subsetXORSum'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "xor_total": "*",
                "max_val": "*",
                "ind#1": "int",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*",
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
def subsetXORSum(var_1):
    ans = 0
    n = len(var_1)
    max_val = 1 << n
    for i in range(1, max_val):
        xor_total = 0
        for j in range(n):
            if i & 1 << j:
                xor_total ^= var_1[j]
        ans += xor_total
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def subsetXORSum(var_1):\n    ans = 0\n    n = len(var_1)\n    max_val = 1 << n\n    for i in range(1, max_val):\n        xor_total = 0\n        for j in range(n):\n            if i & 1 << j:\n                xor_total ^= var_1[j]\n        ans += xor_total\n    return ans"
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
        "subsetXORSum": {
            "name": "subsetXORSum",
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
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
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
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "max_val",
                        "val1": {
                            "name": "LShift",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "max_val",
                            {
                                "name": "LShift",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "n",
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
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "max_val",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "max_val",
                                        "primed": true,
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
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 11
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
                            "i",
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
                            "i",
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
                        "val0": "xor_total",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "xor_total",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                        "val0": "xor_total",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "LShift",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 8,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_total",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                },
                                {
                                    "name": "xor_total",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "xor_total",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "LShift",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 8,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_total",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    },
                                    {
                                        "name": "xor_total",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                "1": "around the beginning of function 'subsetXORSum'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "xor_total": "*",
                "max_val": "*",
                "ind#1": "int",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

