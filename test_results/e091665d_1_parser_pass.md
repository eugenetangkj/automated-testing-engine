# Test Report

Time: 2024-03-30 08:31:49.855444

### Base Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1
```

## Test Case 1

### Modified Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import Counter\nimport heapq\n\ndef findLeastNumOfUniqueInts(arr, k):\n    count = Counter(arr)\n    pq = list(count.values())\n    heapq.heapify(pq)\n    while k > 0:\n        k -= heapq.heappop(pq)\n    return len(pq) if k == 0 else len(pq) + 1"
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
        "from collections import Counter",
        "import heapq"
    ],
    "fncs": {
        "findLeastNumOfUniqueInts": {
            "name": "findLeastNumOfUniqueInts",
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
                },
                {
                    "val0": "k",
                    "val1": "*",
                    "valueArray": [
                        "k",
                        "*"
                    ],
                    "valueList": [
                        "k",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "Counter",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "arr",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "arr",
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
                        "val0": "pq",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "values",
                                    "args": [
                                        {
                                            "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "k",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "k",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "pq",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
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
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "k",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "k",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
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
                                "line": 10
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "k",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "k",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
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
                            "k",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                            "k",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                "1": "around the beginning of function 'findLeastNumOfUniqueInts'",
                "2": "the condition of the 'while' loop at line 8",
                "3": "*after* the 'while' loop starting at line 8",
                "4": "inside the body of the 'while' loop beginning at line 9"
            },
            "types": {
                "pq": "*",
                "count": "*",
                "k": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(var_0, var_1):
    count = Counter(var_0)
    pq = list(count.values())
    heapq.heapify(pq)
    while var_1 > 0:
        var_1 -= heapq.heappop(pq)
    return len(pq) if var_1 == 0 else len(pq) + 1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import Counter\nimport heapq\n\ndef findLeastNumOfUniqueInts(var_0, var_1):\n    count = Counter(var_0)\n    pq = list(count.values())\n    heapq.heapify(pq)\n    while var_1 > 0:\n        var_1 -= heapq.heappop(pq)\n    return len(pq) if var_1 == 0 else len(pq) + 1"
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
        "from collections import Counter",
        "import heapq"
    ],
    "fncs": {
        "findLeastNumOfUniqueInts": {
            "name": "findLeastNumOfUniqueInts",
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
                        "val0": "count",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "Counter",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_0",
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
                        "val0": "pq",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "values",
                                    "args": [
                                        {
                                            "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "var_1",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "pq",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
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
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_1",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_1",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
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
                                "line": 10
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "var_1",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
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
                            "var_1",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                            "var_1",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                "1": "around the beginning of function 'findLeastNumOfUniqueInts'",
                "2": "the condition of the 'while' loop at line 8",
                "3": "*after* the 'while' loop starting at line 8",
                "4": "inside the body of the 'while' loop beginning at line 9"
            },
            "types": {
                "pq": "*",
                "var_1": "*",
                "count": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else 1 + len(pq)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import Counter\nimport heapq\n\ndef findLeastNumOfUniqueInts(arr, k):\n    count = Counter(arr)\n    pq = list(count.values())\n    heapq.heapify(pq)\n    while k > 0:\n        k -= heapq.heappop(pq)\n    return len(pq) if k == 0 else 1 + len(pq)"
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
        "from collections import Counter",
        "import heapq"
    ],
    "fncs": {
        "findLeastNumOfUniqueInts": {
            "name": "findLeastNumOfUniqueInts",
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
                },
                {
                    "val0": "k",
                    "val1": "*",
                    "valueArray": [
                        "k",
                        "*"
                    ],
                    "valueList": [
                        "k",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "Counter",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "arr",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "arr",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "arr",
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
                        "val0": "pq",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "values",
                                    "args": [
                                        {
                                            "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "k",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "k",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 10,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "pq",
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "k",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 10,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "k",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 10,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "k",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "k",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
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
                            "k",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                            "k",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "k",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                "1": "around the beginning of function 'findLeastNumOfUniqueInts'",
                "2": "the condition of the 'while' loop at line 8",
                "3": "*after* the 'while' loop starting at line 8",
                "4": "inside the body of the 'while' loop beginning at line 9"
            },
            "types": {
                "pq": "*",
                "count": "*",
                "k": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(var_2, var_3):
    count = Counter(var_2)
    pq = list(count.values())
    heapq.heapify(pq)
    while var_3 > 0:
        var_3 -= heapq.heappop(pq)
    return len(pq) if var_3 == 0 else 1 + len(pq)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import Counter\nimport heapq\n\ndef findLeastNumOfUniqueInts(var_2, var_3):\n    count = Counter(var_2)\n    pq = list(count.values())\n    heapq.heapify(pq)\n    while var_3 > 0:\n        var_3 -= heapq.heappop(pq)\n    return len(pq) if var_3 == 0 else 1 + len(pq)"
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
        "from collections import Counter",
        "import heapq"
    ],
    "fncs": {
        "findLeastNumOfUniqueInts": {
            "name": "findLeastNumOfUniqueInts",
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
                        "val0": "count",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "Counter",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "Counter",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_2",
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
                        "val0": "pq",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "values",
                                    "args": [
                                        {
                                            "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                            "pq",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "values",
                                        "args": [
                                            {
                                                "name": "count",
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
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "var_3",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "pq",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 10,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "pq",
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_3",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 10,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_3",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "pq",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 10,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "pq",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "var_3",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "heappop",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "heapq",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "pq",
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
                            "var_3",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                            "var_3",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "heappop",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "heapq",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "pq",
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
                "1": "around the beginning of function 'findLeastNumOfUniqueInts'",
                "2": "the condition of the 'while' loop at line 8",
                "3": "*after* the 'while' loop starting at line 8",
                "4": "inside the body of the 'while' loop beginning at line 9"
            },
            "types": {
                "pq": "*",
                "var_3": "*",
                "count": "*"
            }
        }
    }
}
```

</details>

