# Test Report

Time: 2024-03-30 06:28:35.313354

### Base Program

```py
from collections import deque

def mostCompetitive(nums, k):
    stack = deque()
    n = len(nums)
    for i in range(n):
        while stack and stack[-1] > nums[i] and len(stack) + n - i > k:
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])
    return list(stack)
```

## Test Case 1

### Modified Program

```py
from collections import deque

def mostCompetitive(nums, k):
    stack = deque()
    n = len(nums)
    for i in range(n):
        while stack and stack[-1] > nums[i] and (len(stack) + n - i > k):
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])
    return list(stack)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef mostCompetitive(nums, k):\n    stack = deque()\n    n = len(nums)\n    for i in range(n):\n        while stack and stack[-1] > nums[i] and (len(stack) + n - i > k):\n            stack.pop()\n        if len(stack) < k:\n            stack.append(nums[i])\n    return list(stack)"
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
        "from collections import deque"
    ],
    "fncs": {
        "mostCompetitive": {
            "name": "mostCompetitive",
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
                        "val0": "stack",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "stack",
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
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "nums",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
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
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "len",
                                                            "args": [
                                                                {
                                                                    "name": "stack",
                                                                    "primed": false,
                                                                    "line": 7,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 7,
                                                            "tokentype": "Operation"
                                                        },
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
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "k",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
                                                                        "primed": false,
                                                                        "line": 7,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 7,
                                                                "tokentype": "Operation"
                                                            },
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
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
                                                                        "primed": false,
                                                                        "line": 7,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 7,
                                                                "tokentype": "Operation"
                                                            },
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
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
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
                        "val0": "stack",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "stack",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "k",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
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
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "stack",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "pop",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'mostCompetitive'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8"
            },
            "types": {
                "stack": "*",
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
from collections import deque

def mostCompetitive(var_0, var_1):
    stack = deque()
    n = len(var_0)
    for i in range(n):
        while stack and stack[-1] > var_0[i] and (len(stack) + n - i > var_1):
            stack.pop()
        if len(stack) < var_1:
            stack.append(var_0[i])
    return list(stack)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef mostCompetitive(var_0, var_1):\n    stack = deque()\n    n = len(var_0)\n    for i in range(n):\n        while stack and stack[-1] > var_0[i] and (len(stack) + n - i > var_1):\n            stack.pop()\n        if len(stack) < var_1:\n            stack.append(var_0[i])\n    return list(stack)"
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
        "from collections import deque"
    ],
    "fncs": {
        "mostCompetitive": {
            "name": "mostCompetitive",
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
                        "val0": "stack",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "stack",
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
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
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
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "len",
                                                            "args": [
                                                                {
                                                                    "name": "stack",
                                                                    "primed": false,
                                                                    "line": 7,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 7,
                                                            "tokentype": "Operation"
                                                        },
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
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_1",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
                                                                        "primed": false,
                                                                        "line": 7,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 7,
                                                                "tokentype": "Operation"
                                                            },
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
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
                                                                        "primed": false,
                                                                        "line": 7,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 7,
                                                                "tokentype": "Operation"
                                                            },
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
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
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
                        "val0": "stack",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "stack",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "stack",
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
                                    "name": "stack",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
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
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
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
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "stack",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "pop",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'mostCompetitive'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8"
            },
            "types": {
                "stack": "*",
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
from collections import deque

def mostCompetitive(nums, k):
    stack = deque()
    n = len(nums)
    for i in range(n):
        while stack and stack[-1] > nums[i] and (n + len(stack) + -i > k):
            stack.pop()
        if len(stack) < k:
            stack.append(nums[i])
    return list(stack)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef mostCompetitive(nums, k):\n    stack = deque()\n    n = len(nums)\n    for i in range(n):\n        while stack and stack[-1] > nums[i] and (n + len(stack) + -i > k):\n            stack.pop()\n        if len(stack) < k:\n            stack.append(nums[i])\n    return list(stack)"
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
        "from collections import deque"
    ],
    "fncs": {
        "mostCompetitive": {
            "name": "mostCompetitive",
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
                        "val0": "stack",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "stack",
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
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "nums",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
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
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "n",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "len",
                                                            "args": [
                                                                {
                                                                    "name": "stack",
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
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                        {
                                            "name": "k",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
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
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "k",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
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
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "k",
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
                        "val0": "stack",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "stack",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "k",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
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
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "k",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "stack",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "pop",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'mostCompetitive'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8"
            },
            "types": {
                "stack": "*",
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
from collections import deque

def mostCompetitive(var_2, var_3):
    stack = deque()
    n = len(var_2)
    for i in range(n):
        while stack and stack[-1] > var_2[i] and (n + len(stack) + -i > var_3):
            stack.pop()
        if len(stack) < var_3:
            stack.append(var_2[i])
    return list(stack)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef mostCompetitive(var_2, var_3):\n    stack = deque()\n    n = len(var_2)\n    for i in range(n):\n        while stack and stack[-1] > var_2[i] and (n + len(stack) + -i > var_3):\n            stack.pop()\n        if len(stack) < var_3:\n            stack.append(var_2[i])\n    return list(stack)"
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
        "from collections import deque"
    ],
    "fncs": {
        "mostCompetitive": {
            "name": "mostCompetitive",
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
                        "val0": "stack",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
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
                            "n",
                            {
                                "name": "len",
                                "args": [
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
                            "n",
                            {
                                "name": "len",
                                "args": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 6
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
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "stack",
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
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                                "line": 6
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
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "name": "And",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "stack",
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
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_2",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
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
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "n",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "len",
                                                            "args": [
                                                                {
                                                                    "name": "stack",
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
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                        {
                                            "name": "var_3",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_2",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
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
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "var_3",
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
                                "name": "And",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "stack",
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
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_2",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "len",
                                                                "args": [
                                                                    {
                                                                        "name": "stack",
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
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                            {
                                                "name": "var_3",
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
                        "val0": "stack",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "stack",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
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
                                {
                                    "name": "stack",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "stack",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "stack",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
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
                                    {
                                        "name": "stack",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "stack",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "pop",
                                    "args": [
                                        {
                                            "name": "stack",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "stack",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "pop",
                                        "args": [
                                            {
                                                "name": "stack",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                "1": "around the beginning of function 'mostCompetitive'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8"
            },
            "types": {
                "stack": "*",
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

