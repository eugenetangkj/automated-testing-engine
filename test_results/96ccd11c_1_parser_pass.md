# Test Report

Time: 2024-03-30 08:05:15.532739

### Base Program

```py
def bad_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i != nums[j] - nums[i]:
                count += 1
    return count
```

## Test Case 1

### Modified Program

```py
def bad_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i != nums[j] - nums[i]:
                count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def bad_pairs(nums):\n    count = 0\n    for i in range(len(nums)):\n        for j in range(i + 1, len(nums)):\n            if j - i != nums[j] - nums[i]:\n                count += 1\n    return count"
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
        "bad_pairs": {
            "name": "bad_pairs",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
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
                                                "name": "nums",
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
                                                "name": "nums",
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
                            "name": "count",
                            "primed": false,
                            "line": 7,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": true,
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
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "nums",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": true,
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
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": true,
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
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [],
                "7": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                                            "name": "nums",
                                                            "primed": false,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "nums",
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
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
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
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'bad_pairs'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 4",
                "6": "*after* the 'for' loop starting at line 4",
                "7": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "count": "*",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def bad_pairs(var_0):
    count = 0
    for i in range(len(var_0)):
        for j in range(i + 1, len(var_0)):
            if j - i != var_0[j] - var_0[i]:
                count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def bad_pairs(var_0):\n    count = 0\n    for i in range(len(var_0)):\n        for j in range(i + 1, len(var_0)):\n            if j - i != var_0[j] - var_0[i]:\n                count += 1\n    return count"
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
        "bad_pairs": {
            "name": "bad_pairs",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
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
                                                "name": "var_0",
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
                                                "name": "var_0",
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
                            "name": "count",
                            "primed": false,
                            "line": 7,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": true,
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": true,
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": true,
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [],
                "7": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
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
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
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
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'bad_pairs'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 4",
                "6": "*after* the 'for' loop starting at line 4",
                "7": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "count": "*",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def bad_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(1 + i, len(nums)):
            if j + -i != nums[j] + -nums[i]:
                count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def bad_pairs(nums):\n    count = 0\n    for i in range(len(nums)):\n        for j in range(1 + i, len(nums)):\n            if j + -i != nums[j] + -nums[i]:\n                count += 1\n    return count"
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
        "bad_pairs": {
            "name": "bad_pairs",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
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
                                                "name": "nums",
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
                                                "name": "nums",
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
                            "name": "count",
                            "primed": false,
                            "line": 7,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "nums",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [],
                "7": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "nums",
                                                            "primed": false,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "nums",
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
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
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
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'bad_pairs'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 4",
                "6": "*after* the 'for' loop starting at line 4",
                "7": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "count": "*",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def bad_pairs(var_1):
    count = 0
    for i in range(len(var_1)):
        for j in range(1 + i, len(var_1)):
            if j + -i != var_1[j] + -var_1[i]:
                count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def bad_pairs(var_1):\n    count = 0\n    for i in range(len(var_1)):\n        for j in range(1 + i, len(var_1)):\n            if j + -i != var_1[j] + -var_1[i]:\n                count += 1\n    return count"
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
        "bad_pairs": {
            "name": "bad_pairs",
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
                            "name": "count",
                            "primed": false,
                            "line": 7,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 7
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [],
                "7": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "USub",
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
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
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
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
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
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
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
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'bad_pairs'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 4",
                "6": "*after* the 'for' loop starting at line 4",
                "7": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "count": "*",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "j": "*"
            }
        }
    }
}
```

</details>

