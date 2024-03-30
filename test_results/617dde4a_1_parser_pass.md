# Test Report

Time: 2024-03-30 08:22:58.229593

### Base Program

```py
def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist
```

## Test Case 1

### Modified Program

```py
def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1
    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i
    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistToClosest(seats):\n    n = len(seats)\n    maxDist = 0\n    lastPerson = -1\n    for i in range(n):\n        if seats[i] == 1:\n            if lastPerson == -1:\n                maxDist = i\n            else:\n                maxDist = max(maxDist, (i - lastPerson) // 2)\n            lastPerson = i\n    maxDist = max(maxDist, n - 1 - lastPerson)\n    return maxDist"
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
        "maxDistToClosest": {
            "name": "maxDistToClosest",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "seats",
                    "val1": "*",
                    "valueArray": [
                        "seats",
                        "*"
                    ],
                    "valueList": [
                        "seats",
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
                                    "name": "seats",
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
                                        "name": "seats",
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
                                        "name": "seats",
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
                        "val0": "maxDist",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
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
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
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
                                        "name": "n",
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
                                        "name": "n",
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "n",
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
                                        {
                                            "name": "lastPerson",
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
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            {
                                                "name": "lastPerson",
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
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            {
                                                "name": "lastPerson",
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
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "maxDist",
                            "primed": true,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "seats",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
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
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "max",
                                            "args": [
                                                {
                                                    "name": "maxDist",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
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
                                                                    "name": "lastPerson",
                                                                    "primed": false,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 10,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
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
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                        "name": "lastPerson",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                        "name": "lastPerson",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "seats",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "lastPerson",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                "1": "around the beginning of function 'maxDistToClosest'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6"
            },
            "types": {
                "maxDist": "*",
                "lastPerson": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
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
def maxDistToClosest(var_0):
    n = len(var_0)
    maxDist = 0
    lastPerson = -1
    for i in range(n):
        if var_0[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i
    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistToClosest(var_0):\n    n = len(var_0)\n    maxDist = 0\n    lastPerson = -1\n    for i in range(n):\n        if var_0[i] == 1:\n            if lastPerson == -1:\n                maxDist = i\n            else:\n                maxDist = max(maxDist, (i - lastPerson) // 2)\n            lastPerson = i\n    maxDist = max(maxDist, n - 1 - lastPerson)\n    return maxDist"
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
        "maxDistToClosest": {
            "name": "maxDistToClosest",
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
                        "val0": "maxDist",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
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
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
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
                                        "name": "n",
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
                                        "name": "n",
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "n",
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
                                        {
                                            "name": "lastPerson",
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
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            {
                                                "name": "lastPerson",
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
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            {
                                                "name": "lastPerson",
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
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "maxDist",
                            "primed": true,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "ite",
                            "args": [
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
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
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
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "max",
                                            "args": [
                                                {
                                                    "name": "maxDist",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
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
                                                                    "name": "lastPerson",
                                                                    "primed": false,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 10,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
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
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                        "name": "lastPerson",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                        "name": "lastPerson",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
                            "name": "ite",
                            "args": [
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
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "lastPerson",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                "1": "around the beginning of function 'maxDistToClosest'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6"
            },
            "types": {
                "maxDist": "*",
                "lastPerson": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
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
def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1
    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i + -lastPerson) // 2)
            lastPerson = i
    maxDist = max(maxDist, n + -1 + -lastPerson)
    return maxDist
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistToClosest(seats):\n    n = len(seats)\n    maxDist = 0\n    lastPerson = -1\n    for i in range(n):\n        if seats[i] == 1:\n            if lastPerson == -1:\n                maxDist = i\n            else:\n                maxDist = max(maxDist, (i + -lastPerson) // 2)\n            lastPerson = i\n    maxDist = max(maxDist, n + -1 + -lastPerson)\n    return maxDist"
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
        "maxDistToClosest": {
            "name": "maxDistToClosest",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "seats",
                    "val1": "*",
                    "valueArray": [
                        "seats",
                        "*"
                    ],
                    "valueList": [
                        "seats",
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
                                    "name": "seats",
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
                                        "name": "seats",
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
                                        "name": "seats",
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
                        "val0": "maxDist",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
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
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
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
                                        "name": "n",
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
                                        "name": "n",
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "n",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
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
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
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
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
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
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
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
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "maxDist",
                            "primed": true,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "seats",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
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
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "max",
                                            "args": [
                                                {
                                                    "name": "maxDist",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
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
                                                                            "name": "lastPerson",
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
                                                            "value": "2",
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
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                                "name": "lastPerson",
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
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                                "name": "lastPerson",
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
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "seats",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "lastPerson",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "seats",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                "1": "around the beginning of function 'maxDistToClosest'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6"
            },
            "types": {
                "maxDist": "*",
                "lastPerson": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
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
def maxDistToClosest(var_1):
    n = len(var_1)
    maxDist = 0
    lastPerson = -1
    for i in range(n):
        if var_1[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i + -lastPerson) // 2)
            lastPerson = i
    maxDist = max(maxDist, n + -1 + -lastPerson)
    return maxDist
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistToClosest(var_1):\n    n = len(var_1)\n    maxDist = 0\n    lastPerson = -1\n    for i in range(n):\n        if var_1[i] == 1:\n            if lastPerson == -1:\n                maxDist = i\n            else:\n                maxDist = max(maxDist, (i + -lastPerson) // 2)\n            lastPerson = i\n    maxDist = max(maxDist, n + -1 + -lastPerson)\n    return maxDist"
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
        "maxDistToClosest": {
            "name": "maxDistToClosest",
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
                        "val0": "maxDist",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
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
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                            "lastPerson",
                            {
                                "name": "USub",
                                "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
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
                                        "name": "n",
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
                                        "name": "n",
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "n",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
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
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
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
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
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
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
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
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "maxDist",
                            "primed": true,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "maxDist",
                                "primed": true,
                                "line": 13
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
                        "val0": "maxDist",
                        "val1": {
                            "name": "ite",
                            "args": [
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
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "lastPerson",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
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
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "max",
                                            "args": [
                                                {
                                                    "name": "maxDist",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
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
                                                                            "name": "lastPerson",
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
                                                            "value": "2",
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
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxDist",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                                "name": "lastPerson",
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
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "maxDist",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "lastPerson",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
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
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "max",
                                                "args": [
                                                    {
                                                        "name": "maxDist",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
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
                                                                                "name": "lastPerson",
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
                                                                "value": "2",
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
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxDist",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "lastPerson",
                        "val1": {
                            "name": "ite",
                            "args": [
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
                                                    "primed": true,
                                                    "line": 6,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "lastPerson",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "lastPerson",
                            {
                                "name": "ite",
                                "args": [
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
                                                        "primed": true,
                                                        "line": 6,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "lastPerson",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                "1": "around the beginning of function 'maxDistToClosest'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6"
            },
            "types": {
                "maxDist": "*",
                "lastPerson": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "n": "*"
            }
        }
    }
}
```

</details>

