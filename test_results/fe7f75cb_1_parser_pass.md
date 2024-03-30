# Test Report

Time: 2024-03-30 07:13:07.023984

### Base Program

```py
import heapq

def eatenApples(apples, days):
    n = len(apples)
    pq = []
    ans = 0

    for i in range(n + 1):
        if i < n and apples[i] > 0:
            heapq.heappush(pq, (i + days[i], apples[i]))

        while pq and pq[0][0] <= i:
            heapq.heappop(pq)

        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))

    return ans
```

## Test Case 1

### Modified Program

```py
import heapq

def eatenApples(apples, days):
    n = len(apples)
    pq = []
    ans = 0
    for i in range(n + 1):
        if i < n and apples[i] > 0:
            heapq.heappush(pq, (i + days[i], apples[i]))
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef eatenApples(apples, days):\n    n = len(apples)\n    pq = []\n    ans = 0\n    for i in range(n + 1):\n        if i < n and apples[i] > 0:\n            heapq.heappush(pq, (i + days[i], apples[i]))\n        while pq and pq[0][0] <= i:\n            heapq.heappop(pq)\n        if pq:\n            ans += 1\n            curr_apple = heapq.heappop(pq)\n            if curr_apple[1] > 1:\n                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))\n    return ans"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "import heapq"
    ],
    "fncs": {
        "eatenApples": {
            "name": "eatenApples",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "apples",
                    "val1": "*",
                    "valueArray": [
                        "apples",
                        "*"
                    ],
                    "valueList": [
                        "apples",
                        "*"
                    ]
                },
                {
                    "val0": "days",
                    "val1": "*",
                    "valueArray": [
                        "days",
                        "*"
                    ],
                    "valueList": [
                        "days",
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
                                    "name": "apples",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "apples",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "apples",
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
                        "val0": "pq",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LtE",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pq",
                                                            "primed": false,
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
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "i",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "ans",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
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
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "curr_apple",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 14,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "curr_apple",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": []
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
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 2
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'eatenApples'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the 'while' loop at line 10",
                "9": "*after* the 'while' loop starting at line 10",
                "10": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "pq": "*",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "curr_apple": "*",
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
import heapq

def eatenApples(var_0, var_1):
    n = len(var_0)
    pq = []
    ans = 0
    for i in range(n + 1):
        if i < n and var_0[i] > 0:
            heapq.heappush(pq, (i + var_1[i], var_0[i]))
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef eatenApples(var_0, var_1):\n    n = len(var_0)\n    pq = []\n    ans = 0\n    for i in range(n + 1):\n        if i < n and var_0[i] > 0:\n            heapq.heappush(pq, (i + var_1[i], var_0[i]))\n        while pq and pq[0][0] <= i:\n            heapq.heappop(pq)\n        if pq:\n            ans += 1\n            curr_apple = heapq.heappop(pq)\n            if curr_apple[1] > 1:\n                heapq.heappush(pq, (curr_apple[0], curr_apple[1] - 1))\n    return ans"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "import heapq"
    ],
    "fncs": {
        "eatenApples": {
            "name": "eatenApples",
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "pq",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LtE",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pq",
                                                            "primed": false,
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
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "i",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "ans",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
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
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "curr_apple",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 14,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "curr_apple",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": []
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
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 2
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'eatenApples'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the 'while' loop at line 10",
                "9": "*after* the 'while' loop starting at line 10",
                "10": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "pq": "*",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "curr_apple": "*",
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
import heapq

def eatenApples(apples, days):
    n = len(apples)
    pq = []
    ans = 0
    for i in range(1 + n):
        if i < n and apples[i] > 0:
            heapq.heappush(pq, (days[i] + i, apples[i]))
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] + -1))
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef eatenApples(apples, days):\n    n = len(apples)\n    pq = []\n    ans = 0\n    for i in range(1 + n):\n        if i < n and apples[i] > 0:\n            heapq.heappush(pq, (days[i] + i, apples[i]))\n        while pq and pq[0][0] <= i:\n            heapq.heappop(pq)\n        if pq:\n            ans += 1\n            curr_apple = heapq.heappop(pq)\n            if curr_apple[1] > 1:\n                heapq.heappush(pq, (curr_apple[0], curr_apple[1] + -1))\n    return ans"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "import heapq"
    ],
    "fncs": {
        "eatenApples": {
            "name": "eatenApples",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "apples",
                    "val1": "*",
                    "valueArray": [
                        "apples",
                        "*"
                    ],
                    "valueList": [
                        "apples",
                        "*"
                    ]
                },
                {
                    "val0": "days",
                    "val1": "*",
                    "valueArray": [
                        "days",
                        "*"
                    ],
                    "valueList": [
                        "days",
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
                                    "name": "apples",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "apples",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "apples",
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
                        "val0": "pq",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "n",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LtE",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pq",
                                                            "primed": false,
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
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "i",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "ans",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
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
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "curr_apple",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 14,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "curr_apple",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": []
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
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 2
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'eatenApples'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the 'while' loop at line 10",
                "9": "*after* the 'while' loop starting at line 10",
                "10": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "pq": "*",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "curr_apple": "*",
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
import heapq

def eatenApples(var_2, var_3):
    n = len(var_2)
    pq = []
    ans = 0
    for i in range(1 + n):
        if i < n and var_2[i] > 0:
            heapq.heappush(pq, (var_3[i] + i, var_2[i]))
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if pq:
            ans += 1
            curr_apple = heapq.heappop(pq)
            if curr_apple[1] > 1:
                heapq.heappush(pq, (curr_apple[0], curr_apple[1] + -1))
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef eatenApples(var_2, var_3):\n    n = len(var_2)\n    pq = []\n    ans = 0\n    for i in range(1 + n):\n        if i < n and var_2[i] > 0:\n            heapq.heappush(pq, (var_3[i] + i, var_2[i]))\n        while pq and pq[0][0] <= i:\n            heapq.heappop(pq)\n        if pq:\n            ans += 1\n            curr_apple = heapq.heappop(pq)\n            if curr_apple[1] > 1:\n                heapq.heappush(pq, (curr_apple[0], curr_apple[1] + -1))\n    return ans"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "import heapq"
    ],
    "fncs": {
        "eatenApples": {
            "name": "eatenApples",
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "pq",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "pq",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "n",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LtE",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pq",
                                                            "primed": false,
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
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "i",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LtE",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pq",
                                                                "primed": false,
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
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "ans",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
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
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "ans",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
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
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "curr_apple",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "pq",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 14,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 14,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "curr_apple",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "curr_apple",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "pq",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 14,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 14,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "curr_apple",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": []
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
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 2
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'eatenApples'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "8": "the condition of the 'while' loop at line 10",
                "9": "*after* the 'while' loop starting at line 10",
                "10": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "pq": "*",
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "curr_apple": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

