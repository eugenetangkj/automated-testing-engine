# Test Report

Time: 2024-03-30 07:54:00.573900

### Base Program

```py
from collections import defaultdict

def smallestMissingValueSubtree(parents, nums):
    n = len(parents)
    children = defaultdict(set)
    for i in range(1, n):
        children[parents[i]].add(nums[i])

    ans = [0] * n
    dfs(0, parents, nums, children, ans)
    return ans

def dfs(node, parents, nums, children, ans):
    for child in list(children[node]):
        dfs(child, parents, nums, children, ans)
        children[node].remove(child)
        children[node].add(ans[child])
    it = next((x for x in children[node] if x > nums[node]), nums[node] + 1)
    ans[node] = it - 1 if it != nums[node] + 1 else it
```

## Test Case 1

### Modified Program

```py
from collections import defaultdict

def smallestMissingValueSubtree(parents, nums):
    n = len(parents)
    children = defaultdict(set)
    for i in range(1, n):
        children[parents[i]].add(nums[i])
    ans = [0] * n
    dfs(0, parents, nums, children, ans)
    return ans

def dfs(node, parents, nums, children, ans):
    for child in list(children[node]):
        dfs(child, parents, nums, children, ans)
        children[node].remove(child)
        children[node].add(ans[child])
    it = next((x for x in children[node] if x > nums[node]), nums[node] + 1)
    ans[node] = it - 1 if it != nums[node] + 1 else it
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef smallestMissingValueSubtree(parents, nums):\n    n = len(parents)\n    children = defaultdict(set)\n    for i in range(1, n):\n        children[parents[i]].add(nums[i])\n    ans = [0] * n\n    dfs(0, parents, nums, children, ans)\n    return ans\n\ndef dfs(node, parents, nums, children, ans):\n    for child in list(children[node]):\n        dfs(child, parents, nums, children, ans)\n        children[node].remove(child)\n        children[node].add(ans[child])\n    it = next((x for x in children[node] if x > nums[node]), nums[node] + 1)\n    ans[node] = it - 1 if it != nums[node] + 1 else it"
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
        "dfs": {
            "name": "dfs",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "node",
                    "val1": "*",
                    "valueArray": [
                        "node",
                        "*"
                    ],
                    "valueList": [
                        "node",
                        "*"
                    ]
                },
                {
                    "val0": "parents",
                    "val1": "*",
                    "valueArray": [
                        "parents",
                        "*"
                    ],
                    "valueList": [
                        "parents",
                        "*"
                    ]
                },
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
                    "val0": "children",
                    "val1": "*",
                    "valueArray": [
                        "children",
                        "*"
                    ],
                    "valueList": [
                        "children",
                        "*"
                    ]
                },
                {
                    "val0": "ans",
                    "val1": "*",
                    "valueArray": [
                        "ans",
                        "*"
                    ],
                    "valueList": [
                        "ans",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "children",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "node",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "children",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "node",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "children",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "node",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
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
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "it",
                        "val1": {
                            "name": "next",
                            "args": [
                                {
                                    "name": "TupleInit",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": false,
                                            "line": 17,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 17,
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
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "node",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 17,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 17,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 17,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
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
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "node",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
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
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "node",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
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
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "node",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
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
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "node",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 18,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 18,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "it",
                                            "primed": true,
                                            "line": 18,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 18,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 18,
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
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "node",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
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
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "node",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 18,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
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
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "node",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
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
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "node",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 18,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "child",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                        "valueArray": [
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
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
                "1": "around the beginning of function 'dfs'",
                "2": "the condition of the 'for' loop at line 13",
                "3": "*after* the 'for' loop starting at line 13",
                "4": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "iter#1": "int",
                "it": "*",
                "child": "*"
            }
        },
        "smallestMissingValueSubtree": {
            "name": "smallestMissingValueSubtree",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "parents",
                    "val1": "*",
                    "valueArray": [
                        "parents",
                        "*"
                    ],
                    "valueList": [
                        "parents",
                        "*"
                    ]
                },
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "parents",
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
                                        "name": "parents",
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
                                        "name": "parents",
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
                        "val0": "children",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "set",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
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
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 8,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
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
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": true,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
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
                "1": "around the beginning of function 'smallestMissingValueSubtree'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "children": "*",
                "ind#0": "int",
                "ans": "*",
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
from collections import defaultdict

def smallestMissingValueSubtree(var_0, var_1):
    n = len(var_0)
    children = defaultdict(set)
    for i in range(1, n):
        children[var_0[i]].add(var_1[i])
    ans = [0] * n
    dfs(0, var_0, var_1, children, ans)
    return ans

def dfs(var_2, var_3, var_4, var_5, var_6):
    for child in list(var_5[var_2]):
        dfs(child, var_3, var_4, var_5, var_6)
        var_5[var_2].remove(child)
        var_5[var_2].add(var_6[child])
    it = next((x for x in var_5[var_2] if x > var_4[var_2]), var_4[var_2] + 1)
    var_6[var_2] = it - 1 if it != var_4[var_2] + 1 else it
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef smallestMissingValueSubtree(var_0, var_1):\n    n = len(var_0)\n    children = defaultdict(set)\n    for i in range(1, n):\n        children[var_0[i]].add(var_1[i])\n    ans = [0] * n\n    dfs(0, var_0, var_1, children, ans)\n    return ans\n\ndef dfs(var_2, var_3, var_4, var_5, var_6):\n    for child in list(var_5[var_2]):\n        dfs(child, var_3, var_4, var_5, var_6)\n        var_5[var_2].remove(child)\n        var_5[var_2].add(var_6[child])\n    it = next((x for x in var_5[var_2] if x > var_4[var_2]), var_4[var_2] + 1)\n    var_6[var_2] = it - 1 if it != var_4[var_2] + 1 else it"
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
        "dfs": {
            "name": "dfs",
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
                },
                {
                    "val0": "var_6",
                    "val1": "*",
                    "valueArray": [
                        "var_6",
                        "*"
                    ],
                    "valueList": [
                        "var_6",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_5",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_2",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
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
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "it",
                        "val1": {
                            "name": "next",
                            "args": [
                                {
                                    "name": "TupleInit",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": false,
                                            "line": 17,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_4",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 17,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 17,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 17,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ]
                    },
                    {
                        "val0": "var_6",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "var_6",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "var_4",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_2",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 18,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 18,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "it",
                                            "primed": true,
                                            "line": 18,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 18,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 18,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_6",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_2",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 18,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ],
                        "valueList": [
                            "var_6",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_2",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 18,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "child",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                        "valueArray": [
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
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
                "1": "around the beginning of function 'dfs'",
                "2": "the condition of the 'for' loop at line 13",
                "3": "*after* the 'for' loop starting at line 13",
                "4": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "iter#1": "int",
                "it": "*",
                "child": "*"
            }
        },
        "smallestMissingValueSubtree": {
            "name": "smallestMissingValueSubtree",
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
                        "val0": "children",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "set",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
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
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 8,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
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
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "n",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": true,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
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
                "1": "around the beginning of function 'smallestMissingValueSubtree'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "children": "*",
                "ind#0": "int",
                "ans": "*",
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
from collections import defaultdict

def smallestMissingValueSubtree(parents, nums):
    n = len(parents)
    children = defaultdict(set)
    for i in range(1, n):
        children[parents[i]].add(nums[i])
    ans = n * [0]
    dfs(0, parents, nums, children, ans)
    return ans

def dfs(node, parents, nums, children, ans):
    for child in list(children[node]):
        dfs(child, parents, nums, children, ans)
        children[node].remove(child)
        children[node].add(ans[child])
    it = next((x for x in children[node] if x > nums[node]), 1 + nums[node])
    ans[node] = it + -1 if it != 1 + nums[node] else it
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef smallestMissingValueSubtree(parents, nums):\n    n = len(parents)\n    children = defaultdict(set)\n    for i in range(1, n):\n        children[parents[i]].add(nums[i])\n    ans = n * [0]\n    dfs(0, parents, nums, children, ans)\n    return ans\n\ndef dfs(node, parents, nums, children, ans):\n    for child in list(children[node]):\n        dfs(child, parents, nums, children, ans)\n        children[node].remove(child)\n        children[node].add(ans[child])\n    it = next((x for x in children[node] if x > nums[node]), 1 + nums[node])\n    ans[node] = it + -1 if it != 1 + nums[node] else it"
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
        "dfs": {
            "name": "dfs",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "node",
                    "val1": "*",
                    "valueArray": [
                        "node",
                        "*"
                    ],
                    "valueList": [
                        "node",
                        "*"
                    ]
                },
                {
                    "val0": "parents",
                    "val1": "*",
                    "valueArray": [
                        "parents",
                        "*"
                    ],
                    "valueList": [
                        "parents",
                        "*"
                    ]
                },
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
                    "val0": "children",
                    "val1": "*",
                    "valueArray": [
                        "children",
                        "*"
                    ],
                    "valueList": [
                        "children",
                        "*"
                    ]
                },
                {
                    "val0": "ans",
                    "val1": "*",
                    "valueArray": [
                        "ans",
                        "*"
                    ],
                    "valueList": [
                        "ans",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "children",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "node",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "children",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "node",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "children",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "node",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
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
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "it",
                        "val1": {
                            "name": "next",
                            "args": [
                                {
                                    "name": "TupleInit",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": false,
                                            "line": 17,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 17,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "node",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 17,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 17,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "node",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "node",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
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
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "node",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "nums",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "node",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 18,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "it",
                                            "primed": true,
                                            "line": 18,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 18,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 18,
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
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "node",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "node",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
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
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "node",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "node",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "child",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                        "valueArray": [
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
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
                "1": "around the beginning of function 'dfs'",
                "2": "the condition of the 'for' loop at line 13",
                "3": "*after* the 'for' loop starting at line 13",
                "4": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "iter#1": "int",
                "it": "*",
                "child": "*"
            }
        },
        "smallestMissingValueSubtree": {
            "name": "smallestMissingValueSubtree",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "parents",
                    "val1": "*",
                    "valueArray": [
                        "parents",
                        "*"
                    ],
                    "valueList": [
                        "parents",
                        "*"
                    ]
                },
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "parents",
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
                                        "name": "parents",
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
                                        "name": "parents",
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
                        "val0": "children",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "set",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
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
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
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
                        "valueArray": [
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 8,
                                                "tokentype": "Constant"
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": true,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
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
                "1": "around the beginning of function 'smallestMissingValueSubtree'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "children": "*",
                "ind#0": "int",
                "ans": "*",
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
from collections import defaultdict

def smallestMissingValueSubtree(var_7, var_8):
    n = len(var_7)
    children = defaultdict(set)
    for i in range(1, n):
        children[var_7[i]].add(var_8[i])
    ans = n * [0]
    dfs(0, var_7, var_8, children, ans)
    return ans

def dfs(var_9, var_10, var_11, var_12, var_13):
    for child in list(var_12[var_9]):
        dfs(child, var_10, var_11, var_12, var_13)
        var_12[var_9].remove(child)
        var_12[var_9].add(var_13[child])
    it = next((x for x in var_12[var_9] if x > var_11[var_9]), 1 + var_11[var_9])
    var_13[var_9] = it + -1 if it != 1 + var_11[var_9] else it
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\n\ndef smallestMissingValueSubtree(var_7, var_8):\n    n = len(var_7)\n    children = defaultdict(set)\n    for i in range(1, n):\n        children[var_7[i]].add(var_8[i])\n    ans = n * [0]\n    dfs(0, var_7, var_8, children, ans)\n    return ans\n\ndef dfs(var_9, var_10, var_11, var_12, var_13):\n    for child in list(var_12[var_9]):\n        dfs(child, var_10, var_11, var_12, var_13)\n        var_12[var_9].remove(child)\n        var_12[var_9].add(var_13[child])\n    it = next((x for x in var_12[var_9] if x > var_11[var_9]), 1 + var_11[var_9])\n    var_13[var_9] = it + -1 if it != 1 + var_11[var_9] else it"
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
        "dfs": {
            "name": "dfs",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_9",
                    "val1": "*",
                    "valueArray": [
                        "var_9",
                        "*"
                    ],
                    "valueList": [
                        "var_9",
                        "*"
                    ]
                },
                {
                    "val0": "var_10",
                    "val1": "*",
                    "valueArray": [
                        "var_10",
                        "*"
                    ],
                    "valueList": [
                        "var_10",
                        "*"
                    ]
                },
                {
                    "val0": "var_11",
                    "val1": "*",
                    "valueArray": [
                        "var_11",
                        "*"
                    ],
                    "valueList": [
                        "var_11",
                        "*"
                    ]
                },
                {
                    "val0": "var_12",
                    "val1": "*",
                    "valueArray": [
                        "var_12",
                        "*"
                    ],
                    "valueList": [
                        "var_12",
                        "*"
                    ]
                },
                {
                    "val0": "var_13",
                    "val1": "*",
                    "valueArray": [
                        "var_13",
                        "*"
                    ],
                    "valueList": [
                        "var_13",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "list",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_12",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_9",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_12",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_9",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "list",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_12",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_9",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 13
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
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "it",
                        "val1": {
                            "name": "next",
                            "args": [
                                {
                                    "name": "TupleInit",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": false,
                                            "line": 17,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 17,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_11",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_9",
                                                    "primed": false,
                                                    "line": 17,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 17,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 17,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 17,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_11",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_9",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "it",
                            {
                                "name": "next",
                                "args": [
                                    {
                                        "name": "TupleInit",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 17,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 17,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_11",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_9",
                                                        "primed": false,
                                                        "line": 17,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 17,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 17,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 17
                            }
                        ]
                    },
                    {
                        "val0": "var_13",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "var_13",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_9",
                                    "primed": false,
                                    "line": 18,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "var_11",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_9",
                                                                    "primed": false,
                                                                    "line": 18,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 18,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "it",
                                                    "primed": true,
                                                    "line": 18,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 18,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 18,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 18,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "it",
                                            "primed": true,
                                            "line": 18,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 18,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 18,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_13",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_9",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_9",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ],
                        "valueList": [
                            "var_13",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_9",
                                        "primed": false,
                                        "line": 18,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_9",
                                                                        "primed": false,
                                                                        "line": 18,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 18,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "it",
                                                        "primed": true,
                                                        "line": 18,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 18,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 18,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 18,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "it",
                                                "primed": true,
                                                "line": 18,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 18,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 18
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "child",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "child",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                        "valueArray": [
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
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
                "1": "around the beginning of function 'dfs'",
                "2": "the condition of the 'for' loop at line 13",
                "3": "*after* the 'for' loop starting at line 13",
                "4": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "iter#1": "int",
                "it": "*",
                "child": "*"
            }
        },
        "smallestMissingValueSubtree": {
            "name": "smallestMissingValueSubtree",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_7",
                    "val1": "*",
                    "valueArray": [
                        "var_7",
                        "*"
                    ],
                    "valueList": [
                        "var_7",
                        "*"
                    ]
                },
                {
                    "val0": "var_8",
                    "val1": "*",
                    "valueArray": [
                        "var_8",
                        "*"
                    ],
                    "valueList": [
                        "var_8",
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
                                    "name": "var_7",
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
                                        "name": "var_7",
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
                                        "name": "var_7",
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
                        "val0": "children",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "defaultdict",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "set",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "children",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "defaultdict",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "set",
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
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
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
                        "valueArray": [
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 8,
                                                "tokentype": "Constant"
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 8,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": true,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": true,
                                "line": 10
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
                "1": "around the beginning of function 'smallestMissingValueSubtree'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "children": "*",
                "ind#0": "int",
                "ans": "*",
                "i": "*",
                "iter#0": "int",
                "n": "*"
            }
        }
    }
}
```

</details>

