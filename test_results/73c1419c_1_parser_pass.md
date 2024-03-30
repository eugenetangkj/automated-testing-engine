# Test Report

Time: 2024-03-30 07:38:31.477044

### Base Program

```py
from collections import defaultdict

def sum_of_intervals(arr):
    n = len(arr)
    indices = defaultdict(list)
    intervals = [0] * n

    for i in range(n):
        indices[arr[i]].append(i)

    for i in range(n):
        for index in indices[arr[i]]:
            intervals[i] += abs(index - i)

    return intervals
```

## Test Case 1

### Modified Program

```py
from collections import defaultdict

def sum_of_intervals(arr):
    n = len(arr)
    indices = defaultdict(list)
    intervals = [0] * n
    for i in range(n):
        indices[arr[i]].append(i)
    for i in range(n):
        for index in indices[arr[i]]:
            intervals[i] += abs(index - i)
    return intervals
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef sum_of_intervals(arr):\n    n = len(arr)\n    indices = defaultdict(list)\n    intervals = [0] * n\n    for i in range(n):\n        indices[arr[i]].append(i)\n    for i in range(n):\n        for index in indices[arr[i]]:\n            intervals[i] += abs(index - i)\n    return intervals"
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
        "from collections import defaultdict"
    ],
    "fncs": {
        "sum_of_intervals": {
            "name": "sum_of_intervals",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "arr",
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
                                        "name": "arr",
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
                                        "name": "arr",
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
                        "val0": "indices",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "list",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
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
                        "val0": "intervals",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 6,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
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
                                    "name": "n",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
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
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "intervals",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
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
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "iter#2",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "indices",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
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
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 10,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
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
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                "9": [],
                "10": [
                    {
                        "val0": "index",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "intervals",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "intervals",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "intervals",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "abs",
                                            "args": [
                                                {
                                                    "name": "Sub",
                                                    "args": [
                                                        {
                                                            "name": "index",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
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
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'sum_of_intervals'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "5": "the condition of the 'for' loop at line 9",
                "6": "*after* the 'for' loop starting at line 9",
                "7": "inside the body of the 'for' loop beginning at line 10",
                "8": "the condition of the 'for' loop at line 10",
                "9": "*after* the 'for' loop starting at line 10",
                "10": "inside the body of the 'for' loop beginning at line 11"
            },
            "types": {
                "indices": "*",
                "intervals": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "iter#2": "int",
                "i": "*",
                "iter#1": "int",
                "index": "*",
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
from collections import defaultdict

def sum_of_intervals(var_0):
    n = len(var_0)
    indices = defaultdict(list)
    intervals = [0] * n
    for i in range(n):
        indices[var_0[i]].append(i)
    for i in range(n):
        for index in indices[var_0[i]]:
            intervals[i] += abs(index - i)
    return intervals
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef sum_of_intervals(var_0):\n    n = len(var_0)\n    indices = defaultdict(list)\n    intervals = [0] * n\n    for i in range(n):\n        indices[var_0[i]].append(i)\n    for i in range(n):\n        for index in indices[var_0[i]]:\n            intervals[i] += abs(index - i)\n    return intervals"
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
        "from collections import defaultdict"
    ],
    "fncs": {
        "sum_of_intervals": {
            "name": "sum_of_intervals",
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
                        "val0": "indices",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "list",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
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
                        "val0": "intervals",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 6,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
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
                                    "name": "n",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
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
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "intervals",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
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
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "iter#2",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "indices",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
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
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 10,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
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
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                "9": [],
                "10": [
                    {
                        "val0": "index",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "intervals",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "intervals",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "intervals",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "abs",
                                            "args": [
                                                {
                                                    "name": "Sub",
                                                    "args": [
                                                        {
                                                            "name": "index",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
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
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'sum_of_intervals'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "5": "the condition of the 'for' loop at line 9",
                "6": "*after* the 'for' loop starting at line 9",
                "7": "inside the body of the 'for' loop beginning at line 10",
                "8": "the condition of the 'for' loop at line 10",
                "9": "*after* the 'for' loop starting at line 10",
                "10": "inside the body of the 'for' loop beginning at line 11"
            },
            "types": {
                "indices": "*",
                "intervals": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "iter#2": "int",
                "i": "*",
                "iter#1": "int",
                "index": "*",
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
from collections import defaultdict

def sum_of_intervals(arr):
    n = len(arr)
    indices = defaultdict(list)
    intervals = n * [0]
    for i in range(n):
        indices[arr[i]].append(i)
    for i in range(n):
        for index in indices[arr[i]]:
            intervals[i] += abs(index + -i)
    return intervals
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef sum_of_intervals(arr):\n    n = len(arr)\n    indices = defaultdict(list)\n    intervals = n * [0]\n    for i in range(n):\n        indices[arr[i]].append(i)\n    for i in range(n):\n        for index in indices[arr[i]]:\n            intervals[i] += abs(index + -i)\n    return intervals"
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
        "from collections import defaultdict"
    ],
    "fncs": {
        "sum_of_intervals": {
            "name": "sum_of_intervals",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "arr",
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
                                        "name": "arr",
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
                                        "name": "arr",
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
                        "val0": "indices",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "list",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
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
                        "val0": "intervals",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
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
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
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
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
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
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "intervals",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
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
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "iter#2",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "indices",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
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
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 10,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
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
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                "9": [],
                "10": [
                    {
                        "val0": "index",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "intervals",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "intervals",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "intervals",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "abs",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "index",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "USub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
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
                        "valueArray": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "USub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "USub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                "1": "around the beginning of function 'sum_of_intervals'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "5": "the condition of the 'for' loop at line 9",
                "6": "*after* the 'for' loop starting at line 9",
                "7": "inside the body of the 'for' loop beginning at line 10",
                "8": "the condition of the 'for' loop at line 10",
                "9": "*after* the 'for' loop starting at line 10",
                "10": "inside the body of the 'for' loop beginning at line 11"
            },
            "types": {
                "indices": "*",
                "intervals": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "iter#2": "int",
                "i": "*",
                "iter#1": "int",
                "index": "*",
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
from collections import defaultdict

def sum_of_intervals(var_1):
    n = len(var_1)
    indices = defaultdict(list)
    intervals = n * [0]
    for i in range(n):
        indices[var_1[i]].append(i)
    for i in range(n):
        for index in indices[var_1[i]]:
            intervals[i] += abs(index + -i)
    return intervals
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef sum_of_intervals(var_1):\n    n = len(var_1)\n    indices = defaultdict(list)\n    intervals = n * [0]\n    for i in range(n):\n        indices[var_1[i]].append(i)\n    for i in range(n):\n        for index in indices[var_1[i]]:\n            intervals[i] += abs(index + -i)\n    return intervals"
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
        "from collections import defaultdict"
    ],
    "fncs": {
        "sum_of_intervals": {
            "name": "sum_of_intervals",
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
                                        "name": "var_1",
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
                                        "name": "var_1",
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
                        "val0": "indices",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "list",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "indices",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "list",
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
                        "val0": "intervals",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
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
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
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
                            "intervals",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
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
                                        "name": "n",
                                        "primed": true,
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
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 9
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
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "intervals",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "intervals",
                                "primed": false,
                                "line": 12
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
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
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
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
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
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                        "val0": "iter#2",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "indices",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
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
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                            "iter#2",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "indices",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
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
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 10,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 10
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
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
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
                "9": [],
                "10": [
                    {
                        "val0": "index",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "intervals",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "intervals",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "intervals",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "abs",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "index",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "USub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
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
                        "valueArray": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "USub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "intervals",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "intervals",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "intervals",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "abs",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "index",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "USub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                "1": "around the beginning of function 'sum_of_intervals'",
                "2": "the condition of the 'for' loop at line 7",
                "3": "*after* the 'for' loop starting at line 7",
                "4": "inside the body of the 'for' loop beginning at line 8",
                "5": "the condition of the 'for' loop at line 9",
                "6": "*after* the 'for' loop starting at line 9",
                "7": "inside the body of the 'for' loop beginning at line 10",
                "8": "the condition of the 'for' loop at line 10",
                "9": "*after* the 'for' loop starting at line 10",
                "10": "inside the body of the 'for' loop beginning at line 11"
            },
            "types": {
                "indices": "*",
                "intervals": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "iter#2": "int",
                "i": "*",
                "iter#1": "int",
                "index": "*",
                "iter#0": "int",
                "n": "*"
            }
        }
    }
}
```

</details>

