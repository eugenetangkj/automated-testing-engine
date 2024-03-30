# Test Report

Time: 2024-03-30 07:54:30.403491

### Base Program

```py
def check_arithmetic_subarrays(nums, l, r):
    results = []
    for i in range(len(l)):
        subarray = sorted(nums[l[i]:r[i] + 1])
        is_arithmetic = True
        diff = subarray[1] - subarray[0]
        for j in range(1, len(subarray) - 1):
            if subarray[j + 1] - subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results
```

## Test Case 1

### Modified Program

```py
def check_arithmetic_subarrays(nums, l, r):
    results = []
    for i in range(len(l)):
        subarray = sorted(nums[l[i]:r[i] + 1])
        is_arithmetic = True
        diff = subarray[1] - subarray[0]
        for j in range(1, len(subarray) - 1):
            if subarray[j + 1] - subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def check_arithmetic_subarrays(nums, l, r):\n    results = []\n    for i in range(len(l)):\n        subarray = sorted(nums[l[i]:r[i] + 1])\n        is_arithmetic = True\n        diff = subarray[1] - subarray[0]\n        for j in range(1, len(subarray) - 1):\n            if subarray[j + 1] - subarray[j] != diff:\n                is_arithmetic = False\n                break\n        results.append(is_arithmetic)\n    return results"
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
        "check_arithmetic_subarrays": {
            "name": "check_arithmetic_subarrays",
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
                    "val0": "l",
                    "val1": "*",
                    "valueArray": [
                        "l",
                        "*"
                    ],
                    "valueList": [
                        "l",
                        "*"
                    ]
                },
                {
                    "val0": "r",
                    "val1": "*",
                    "valueArray": [
                        "r",
                        "*"
                    ],
                    "valueList": [
                        "r",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "results",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "l",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "l",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "l",
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
                            "name": "results",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "results",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "results",
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
                            "i",
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
                            "i",
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
                        "val0": "subarray",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "nums",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "l",
                                                            "primed": false,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "r",
                                                                    "primed": false,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                    "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "l",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "r",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "l",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "r",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "True",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "0",
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
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0",
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
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0",
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                        "val0": "results",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "results",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "is_arithmetic",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "NotEq",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "j",
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
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                {
                                    "name": "diff",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "j",
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
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "j",
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
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "False",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
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
                "1": "around the beginning of function 'check_arithmetic_subarrays'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the if-statement at line 8",
                "9": "inside the if-branch starting at line 9",
                "11": "after the if-statement beginning at line 8"
            },
            "types": {
                "is_arithmetic": "*",
                "ind#1": "int",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "diff": "*",
                "j": "*",
                "results": "*",
                "subarray": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def check_arithmetic_subarrays(var_0, var_1, var_2):
    results = []
    for i in range(len(var_1)):
        subarray = sorted(var_0[var_1[i]:var_2[i] + 1])
        is_arithmetic = True
        diff = subarray[1] - subarray[0]
        for j in range(1, len(subarray) - 1):
            if subarray[j + 1] - subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def check_arithmetic_subarrays(var_0, var_1, var_2):\n    results = []\n    for i in range(len(var_1)):\n        subarray = sorted(var_0[var_1[i]:var_2[i] + 1])\n        is_arithmetic = True\n        diff = subarray[1] - subarray[0]\n        for j in range(1, len(subarray) - 1):\n            if subarray[j + 1] - subarray[j] != diff:\n                is_arithmetic = False\n                break\n        results.append(is_arithmetic)\n    return results"
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
        "check_arithmetic_subarrays": {
            "name": "check_arithmetic_subarrays",
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
                        "val0": "results",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
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
                                    "line": 3,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
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
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
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
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
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
                            "name": "results",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "results",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "results",
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
                            "i",
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
                            "i",
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
                        "val0": "subarray",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "var_2",
                                                                    "primed": false,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                    "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_2",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_2",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "True",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "0",
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
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0",
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
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0",
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                        "val0": "results",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "results",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "is_arithmetic",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "NotEq",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "j",
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
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                {
                                    "name": "diff",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "j",
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
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "j",
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
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "False",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
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
                "1": "around the beginning of function 'check_arithmetic_subarrays'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the if-statement at line 8",
                "9": "inside the if-branch starting at line 9",
                "11": "after the if-statement beginning at line 8"
            },
            "types": {
                "is_arithmetic": "*",
                "ind#1": "int",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "diff": "*",
                "j": "*",
                "results": "*",
                "subarray": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def check_arithmetic_subarrays(nums, l, r):
    results = []
    for i in range(len(l)):
        subarray = sorted(nums[l[i]:1 + r[i]])
        is_arithmetic = True
        diff = subarray[1] + -subarray[0]
        for j in range(1, len(subarray) + -1):
            if subarray[1 + j] + -subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def check_arithmetic_subarrays(nums, l, r):\n    results = []\n    for i in range(len(l)):\n        subarray = sorted(nums[l[i]:1 + r[i]])\n        is_arithmetic = True\n        diff = subarray[1] + -subarray[0]\n        for j in range(1, len(subarray) + -1):\n            if subarray[1 + j] + -subarray[j] != diff:\n                is_arithmetic = False\n                break\n        results.append(is_arithmetic)\n    return results"
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
        "check_arithmetic_subarrays": {
            "name": "check_arithmetic_subarrays",
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
                    "val0": "l",
                    "val1": "*",
                    "valueArray": [
                        "l",
                        "*"
                    ],
                    "valueList": [
                        "l",
                        "*"
                    ]
                },
                {
                    "val0": "r",
                    "val1": "*",
                    "valueArray": [
                        "r",
                        "*"
                    ],
                    "valueList": [
                        "r",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "results",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "l",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "l",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "l",
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
                            "name": "results",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "results",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "results",
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
                            "i",
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
                            "i",
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
                        "val0": "subarray",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "nums",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "l",
                                                            "primed": false,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "r",
                                                                    "primed": false,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                {
                                                    "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "l",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "r",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                    {
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "l",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "r",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                    {
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "True",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
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
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
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
                            "diff",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
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
                            "diff",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
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
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 7,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
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
                        "val0": "results",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "results",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "is_arithmetic",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "NotEq",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 8,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "subarray",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "diff",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 8,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "subarray",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 8,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "subarray",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "False",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
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
                "1": "around the beginning of function 'check_arithmetic_subarrays'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the if-statement at line 8",
                "9": "inside the if-branch starting at line 9",
                "11": "after the if-statement beginning at line 8"
            },
            "types": {
                "is_arithmetic": "*",
                "ind#1": "int",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "diff": "*",
                "j": "*",
                "results": "*",
                "subarray": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def check_arithmetic_subarrays(var_3, var_4, var_5):
    results = []
    for i in range(len(var_4)):
        subarray = sorted(var_3[var_4[i]:1 + var_5[i]])
        is_arithmetic = True
        diff = subarray[1] + -subarray[0]
        for j in range(1, len(subarray) + -1):
            if subarray[1 + j] + -subarray[j] != diff:
                is_arithmetic = False
                break
        results.append(is_arithmetic)
    return results
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def check_arithmetic_subarrays(var_3, var_4, var_5):\n    results = []\n    for i in range(len(var_4)):\n        subarray = sorted(var_3[var_4[i]:1 + var_5[i]])\n        is_arithmetic = True\n        diff = subarray[1] + -subarray[0]\n        for j in range(1, len(subarray) + -1):\n            if subarray[1 + j] + -subarray[j] != diff:\n                is_arithmetic = False\n                break\n        results.append(is_arithmetic)\n    return results"
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
        "check_arithmetic_subarrays": {
            "name": "check_arithmetic_subarrays",
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
                        "val0": "results",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_4",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_4",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_4",
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
                            "name": "results",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "results",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "results",
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
                            "i",
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
                            "i",
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
                        "val0": "subarray",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": false,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "var_5",
                                                                    "primed": false,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                {
                                                    "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                    {
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "subarray",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                    {
                                                        "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "True",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "True",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "subarray",
                                            "primed": true,
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
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
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
                            "diff",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
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
                            "diff",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "subarray",
                                                "primed": true,
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
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
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 7,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
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
                        "val0": "results",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "results",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "is_arithmetic",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "results",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "results",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "is_arithmetic",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "NotEq",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "subarray",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 8,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "subarray",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "diff",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 8,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "subarray",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "NotEq",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "subarray",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 8,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "subarray",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "diff",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "is_arithmetic",
                        "val1": {
                            "value": "False",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "is_arithmetic",
                            {
                                "value": "False",
                                "line": 9
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
                "1": "around the beginning of function 'check_arithmetic_subarrays'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the if-statement at line 8",
                "9": "inside the if-branch starting at line 9",
                "11": "after the if-statement beginning at line 8"
            },
            "types": {
                "is_arithmetic": "*",
                "ind#1": "int",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "diff": "*",
                "j": "*",
                "results": "*",
                "subarray": "*"
            }
        }
    }
}
```

</details>

