# Test Report

Time: 2024-03-30 07:51:58.544490

### Base Program

```py
def pancakeSort(arr):
    flips = []
    for size in range(len(arr), 1, -1):
        maxIdx = arr.index(max(arr[:size]))
        flips.extend([maxIdx + 1, size])
        arr[:maxIdx + 1] = reversed(arr[:maxIdx + 1])
        arr[:size] = reversed(arr[:size])
    return flips
```

## Test Case 1

### Modified Program

```py
def pancakeSort(arr):
    flips = []
    for size in range(len(arr), 1, -1):
        maxIdx = arr.index(max(arr[:size]))
        flips.extend([maxIdx + 1, size])
        arr[:maxIdx + 1] = reversed(arr[:maxIdx + 1])
        arr[:size] = reversed(arr[:size])
    return flips
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def pancakeSort(arr):\n    flips = []\n    for size in range(len(arr), 1, -1):\n        maxIdx = arr.index(max(arr[:size]))\n        flips.extend([maxIdx + 1, size])\n        arr[:maxIdx + 1] = reversed(arr[:maxIdx + 1])\n        arr[:size] = reversed(arr[:size])\n    return flips"
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
        "pancakeSort": {
            "name": "pancakeSort",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "arr",
                    "val1": "*",
                    "valueArray": [
                        "arr",
                        "*"
                    ],
                    "valueList": [
                        "arr",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "flips",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flips",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flips",
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
                                            "name": "arr",
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
                                },
                                {
                                    "name": "USub",
                                    "args": [
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
                                                "name": "arr",
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
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                                                "name": "arr",
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
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                            "name": "flips",
                            "primed": false,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "size",
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
                            "size",
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
                            "size",
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
                        "val0": "maxIdx",
                        "val1": {
                            "name": "index",
                            "args": [
                                {
                                    "name": "arr",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                        "val0": "flips",
                        "val1": {
                            "name": "extend",
                            "args": [
                                {
                                    "name": "flips",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "maxIdx",
                                                    "primed": true,
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
                                        {
                                            "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
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
                                            {
                                                "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
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
                                            {
                                                "name": "size",
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
                        "val0": "arr",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "maxIdx",
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
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "reversed",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "arr",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "name": "Add",
                                                                    "args": [
                                                                        {
                                                                            "name": "maxIdx",
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
                                                                    "value": "None",
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
                                {
                                    "name": "Slice",
                                    "args": [
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "size",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "reversed",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "AssignElement",
                                                    "args": [
                                                        {
                                                            "name": "arr",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "name": "Add",
                                                                    "args": [
                                                                        {
                                                                            "name": "maxIdx",
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
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "reversed",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "arr",
                                                                            "primed": false,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "Slice",
                                                                            "args": [
                                                                                {
                                                                                    "value": "None",
                                                                                    "line": 6,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "name": "Add",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "maxIdx",
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
                                                                                    "value": "None",
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
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "arr",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "maxIdx",
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
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "arr",
                                                                                "primed": false,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
                                                                                        "line": 6,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "maxIdx",
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
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "arr",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "maxIdx",
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
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "arr",
                                                                                "primed": false,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
                                                                                        "line": 6,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "maxIdx",
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
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
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
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'pancakeSort'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "size": "*",
                "flips": "*",
                "ind#0": "int",
                "maxIdx": "*",
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
def pancakeSort(var_0):
    flips = []
    for size in range(len(var_0), 1, -1):
        maxIdx = var_0.index(max(var_0[:size]))
        flips.extend([maxIdx + 1, size])
        var_0[:maxIdx + 1] = reversed(var_0[:maxIdx + 1])
        var_0[:size] = reversed(var_0[:size])
    return flips
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def pancakeSort(var_0):\n    flips = []\n    for size in range(len(var_0), 1, -1):\n        maxIdx = var_0.index(max(var_0[:size]))\n        flips.extend([maxIdx + 1, size])\n        var_0[:maxIdx + 1] = reversed(var_0[:maxIdx + 1])\n        var_0[:size] = reversed(var_0[:size])\n    return flips"
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
        "pancakeSort": {
            "name": "pancakeSort",
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
                        "val0": "flips",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flips",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flips",
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
                                            "name": "var_0",
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
                                },
                                {
                                    "name": "USub",
                                    "args": [
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
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                            "name": "flips",
                            "primed": false,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "size",
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
                            "size",
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
                            "size",
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
                        "val0": "maxIdx",
                        "val1": {
                            "name": "index",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
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
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
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
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
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
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                        "val0": "flips",
                        "val1": {
                            "name": "extend",
                            "args": [
                                {
                                    "name": "flips",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "maxIdx",
                                                    "primed": true,
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
                                        {
                                            "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
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
                                            {
                                                "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
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
                                            {
                                                "name": "size",
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
                        "val0": "var_0",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "maxIdx",
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
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "reversed",
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
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "name": "Add",
                                                                    "args": [
                                                                        {
                                                                            "name": "maxIdx",
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
                                                                    "value": "None",
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
                                {
                                    "name": "Slice",
                                    "args": [
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "size",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "reversed",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "AssignElement",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "name": "Add",
                                                                    "args": [
                                                                        {
                                                                            "name": "maxIdx",
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
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "reversed",
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
                                                                            "name": "Slice",
                                                                            "args": [
                                                                                {
                                                                                    "value": "None",
                                                                                    "line": 6,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "name": "Add",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "maxIdx",
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
                                                                                    "value": "None",
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
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_0",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "maxIdx",
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
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
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
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
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
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
                                                                                        "line": 6,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "maxIdx",
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
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "var_0",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "maxIdx",
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
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
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
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "Add",
                                                                        "args": [
                                                                            {
                                                                                "name": "maxIdx",
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
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
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
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
                                                                                        "line": 6,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "maxIdx",
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
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
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
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'pancakeSort'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "size": "*",
                "flips": "*",
                "ind#0": "int",
                "maxIdx": "*",
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
def pancakeSort(arr):
    flips = []
    for size in range(len(arr), 1, -1):
        maxIdx = arr.index(max(arr[:size]))
        flips.extend([1 + maxIdx, size])
        arr[:1 + maxIdx] = reversed(arr[:1 + maxIdx])
        arr[:size] = reversed(arr[:size])
    return flips
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def pancakeSort(arr):\n    flips = []\n    for size in range(len(arr), 1, -1):\n        maxIdx = arr.index(max(arr[:size]))\n        flips.extend([1 + maxIdx, size])\n        arr[:1 + maxIdx] = reversed(arr[:1 + maxIdx])\n        arr[:size] = reversed(arr[:size])\n    return flips"
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
        "pancakeSort": {
            "name": "pancakeSort",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "arr",
                    "val1": "*",
                    "valueArray": [
                        "arr",
                        "*"
                    ],
                    "valueList": [
                        "arr",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "flips",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flips",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flips",
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
                                            "name": "arr",
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
                                },
                                {
                                    "name": "USub",
                                    "args": [
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
                                                "name": "arr",
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
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                                                "name": "arr",
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
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                            "name": "flips",
                            "primed": false,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "size",
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
                            "size",
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
                            "size",
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
                        "val0": "maxIdx",
                        "val1": {
                            "name": "index",
                            "args": [
                                {
                                    "name": "arr",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                        "val0": "flips",
                        "val1": {
                            "name": "extend",
                            "args": [
                                {
                                    "name": "flips",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "maxIdx",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "size",
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
                        "val0": "arr",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "value": "None",
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
                                                            "name": "maxIdx",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "reversed",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "arr",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
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
                                                                            "name": "maxIdx",
                                                                            "primed": true,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "None",
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
                                {
                                    "name": "Slice",
                                    "args": [
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "size",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "reversed",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "AssignElement",
                                                    "args": [
                                                        {
                                                            "name": "arr",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
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
                                                                            "name": "maxIdx",
                                                                            "primed": true,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "reversed",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "arr",
                                                                            "primed": false,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "Slice",
                                                                            "args": [
                                                                                {
                                                                                    "value": "None",
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
                                                                                            "name": "maxIdx",
                                                                                            "primed": true,
                                                                                            "line": 6,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 6,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "value": "None",
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
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "arr",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
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
                                                                "name": "maxIdx",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "arr",
                                                                                "primed": false,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
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
                                                                                                "name": "maxIdx",
                                                                                                "primed": true,
                                                                                                "line": 6,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 6,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "arr",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
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
                                                                "name": "maxIdx",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "arr",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "arr",
                                                                                "primed": false,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
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
                                                                                                "name": "maxIdx",
                                                                                                "primed": true,
                                                                                                "line": 6,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 6,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
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
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'pancakeSort'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "size": "*",
                "flips": "*",
                "ind#0": "int",
                "maxIdx": "*",
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
def pancakeSort(var_1):
    flips = []
    for size in range(len(var_1), 1, -1):
        maxIdx = var_1.index(max(var_1[:size]))
        flips.extend([1 + maxIdx, size])
        var_1[:1 + maxIdx] = reversed(var_1[:1 + maxIdx])
        var_1[:size] = reversed(var_1[:size])
    return flips
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def pancakeSort(var_1):\n    flips = []\n    for size in range(len(var_1), 1, -1):\n        maxIdx = var_1.index(max(var_1[:size]))\n        flips.extend([1 + maxIdx, size])\n        var_1[:1 + maxIdx] = reversed(var_1[:1 + maxIdx])\n        var_1[:size] = reversed(var_1[:size])\n    return flips"
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
        "pancakeSort": {
            "name": "pancakeSort",
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
                        "val0": "flips",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flips",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flips",
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
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "USub",
                                    "args": [
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
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
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
                            "name": "flips",
                            "primed": false,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "flips",
                                "primed": false,
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "size",
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
                            "size",
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
                            "size",
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
                        "val0": "maxIdx",
                        "val1": {
                            "name": "index",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
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
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
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
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                            "maxIdx",
                            {
                                "name": "index",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
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
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
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
                        "val0": "flips",
                        "val1": {
                            "name": "extend",
                            "args": [
                                {
                                    "name": "flips",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "maxIdx",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "size",
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
                            "flips",
                            {
                                "name": "extend",
                                "args": [
                                    {
                                        "name": "flips",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "maxIdx",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "size",
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
                        "val0": "var_1",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Slice",
                                            "args": [
                                                {
                                                    "value": "None",
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
                                                            "name": "maxIdx",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "None",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "reversed",
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
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
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
                                                                            "name": "maxIdx",
                                                                            "primed": true,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "None",
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
                                {
                                    "name": "Slice",
                                    "args": [
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "size",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "reversed",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "AssignElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "value": "None",
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
                                                                            "name": "maxIdx",
                                                                            "primed": true,
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "None",
                                                                    "line": 6,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "reversed",
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
                                                                            "name": "Slice",
                                                                            "args": [
                                                                                {
                                                                                    "value": "None",
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
                                                                                            "name": "maxIdx",
                                                                                            "primed": true,
                                                                                            "line": 6,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 6,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "value": "None",
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
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "size",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_1",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
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
                                                                "name": "maxIdx",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
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
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
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
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
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
                                                                                                "name": "maxIdx",
                                                                                                "primed": true,
                                                                                                "line": 6,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 6,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Slice",
                                                "args": [
                                                    {
                                                        "value": "None",
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
                                                                "name": "maxIdx",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "None",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "reversed",
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
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                                    {
                                        "name": "Slice",
                                        "args": [
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "size",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "reversed",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "AssignElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "value": "None",
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
                                                                                "name": "maxIdx",
                                                                                "primed": true,
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 6,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "reversed",
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
                                                                                "name": "Slice",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "None",
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
                                                                                                "name": "maxIdx",
                                                                                                "primed": true,
                                                                                                "line": 6,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 6,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "None",
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
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "size",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 7
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
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'pancakeSort'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "size": "*",
                "flips": "*",
                "ind#0": "int",
                "maxIdx": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

