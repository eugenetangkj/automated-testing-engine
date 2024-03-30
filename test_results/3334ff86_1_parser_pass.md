# Test Report

Time: 2024-03-30 06:27:57.458643

### Base Program

```py
from collections import deque

def deckRevealedIncreasing(deck):
    n = len(deck)
    index = deque(range(n))
    ans = [0] * n

    deck.sort()
    for card in deck:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())

    return ans
```

## Test Case 1

### Modified Program

```py
from collections import deque

def deckRevealedIncreasing(deck):
    n = len(deck)
    index = deque(range(n))
    ans = [0] * n
    deck.sort()
    for card in deck:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef deckRevealedIncreasing(deck):\n    n = len(deck)\n    index = deque(range(n))\n    ans = [0] * n\n    deck.sort()\n    for card in deck:\n        ans[index.popleft()] = card\n        if index:\n            index.append(index.popleft())\n    return ans"
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
        "deckRevealedIncreasing": {
            "name": "deckRevealedIncreasing",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "deck",
                    "val1": "*",
                    "valueArray": [
                        "deck",
                        "*"
                    ],
                    "valueList": [
                        "deck",
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
                                    "name": "deck",
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
                                        "name": "deck",
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
                                        "name": "deck",
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
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
                                    "line": 5,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
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
                            "ans",
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
                            "ans",
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
                        "val0": "deck",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "deck",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "deck",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "deck",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "deck",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "deck",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "deck",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "deck",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "deck",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "card",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "popleft",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "card",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "FuncCall",
                                            "args": [
                                                {
                                                    "value": "popleft",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "index",
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
                                },
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                "1": "around the beginning of function 'deckRevealedIncreasing'",
                "2": "the condition of the 'for' loop at line 8",
                "3": "*after* the 'for' loop starting at line 8",
                "4": "inside the body of the 'for' loop beginning at line 9"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "index": "*",
                "iter#0": "int",
                "n": "*",
                "card": "*"
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

def deckRevealedIncreasing(var_0):
    n = len(var_0)
    index = deque(range(n))
    ans = [0] * n
    var_0.sort()
    for card in var_0:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef deckRevealedIncreasing(var_0):\n    n = len(var_0)\n    index = deque(range(n))\n    ans = [0] * n\n    var_0.sort()\n    for card in var_0:\n        ans[index.popleft()] = card\n        if index:\n            index.append(index.popleft())\n    return ans"
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
        "deckRevealedIncreasing": {
            "name": "deckRevealedIncreasing",
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
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
                                    "line": 5,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
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
                            "ans",
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
                            "ans",
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
                        "val0": "var_0",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_0",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "var_0",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_0",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_0",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "card",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "popleft",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "card",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "FuncCall",
                                            "args": [
                                                {
                                                    "value": "popleft",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "index",
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
                                },
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                "1": "around the beginning of function 'deckRevealedIncreasing'",
                "2": "the condition of the 'for' loop at line 8",
                "3": "*after* the 'for' loop starting at line 8",
                "4": "inside the body of the 'for' loop beginning at line 9"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "index": "*",
                "iter#0": "int",
                "n": "*",
                "card": "*"
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

def deckRevealedIncreasing(deck):
    n = len(deck)
    index = deque(range(n))
    ans = n * [0]
    deck.sort()
    for card in deck:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef deckRevealedIncreasing(deck):\n    n = len(deck)\n    index = deque(range(n))\n    ans = n * [0]\n    deck.sort()\n    for card in deck:\n        ans[index.popleft()] = card\n        if index:\n            index.append(index.popleft())\n    return ans"
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
        "deckRevealedIncreasing": {
            "name": "deckRevealedIncreasing",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "deck",
                    "val1": "*",
                    "valueArray": [
                        "deck",
                        "*"
                    ],
                    "valueList": [
                        "deck",
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
                                    "name": "deck",
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
                                        "name": "deck",
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
                                        "name": "deck",
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
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
                                    "line": 5,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
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
                            "ans",
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
                            "ans",
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
                        "val0": "deck",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "deck",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "deck",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "deck",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "deck",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "deck",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "deck",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "deck",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "deck",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "card",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "popleft",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "card",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "FuncCall",
                                            "args": [
                                                {
                                                    "value": "popleft",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "index",
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
                                },
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                "1": "around the beginning of function 'deckRevealedIncreasing'",
                "2": "the condition of the 'for' loop at line 8",
                "3": "*after* the 'for' loop starting at line 8",
                "4": "inside the body of the 'for' loop beginning at line 9"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "index": "*",
                "iter#0": "int",
                "n": "*",
                "card": "*"
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

def deckRevealedIncreasing(var_1):
    n = len(var_1)
    index = deque(range(n))
    ans = n * [0]
    var_1.sort()
    for card in var_1:
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import deque\n\ndef deckRevealedIncreasing(var_1):\n    n = len(var_1)\n    index = deque(range(n))\n    ans = n * [0]\n    var_1.sort()\n    for card in var_1:\n        ans[index.popleft()] = card\n        if index:\n            index.append(index.popleft())\n    return ans"
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
        "deckRevealedIncreasing": {
            "name": "deckRevealedIncreasing",
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "deque",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
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
                                    "line": 5,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "deque",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
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
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ans",
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
                            "ans",
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
                            "ans",
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
                        "val0": "var_1",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_1",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_1",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "card",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "card",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "popleft",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "card",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "popleft",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "card",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "FuncCall",
                                            "args": [
                                                {
                                                    "value": "popleft",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "index",
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
                                },
                                {
                                    "name": "index",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "FuncCall",
                                                "args": [
                                                    {
                                                        "value": "popleft",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "index",
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
                                    },
                                    {
                                        "name": "index",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
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
                "1": "around the beginning of function 'deckRevealedIncreasing'",
                "2": "the condition of the 'for' loop at line 8",
                "3": "*after* the 'for' loop starting at line 8",
                "4": "inside the body of the 'for' loop beginning at line 9"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "index": "*",
                "iter#0": "int",
                "n": "*",
                "card": "*"
            }
        }
    }
}
```

</details>

