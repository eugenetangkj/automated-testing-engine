# Test Report

Time: 2024-03-30 07:25:54.429607

### Base Program

```py
def flip_trees(n, queries):
    flipped_nodes = {}
    for query in queries:
        flipped_nodes[query] = not flipped_nodes.get(query, False)
        while query > 1:
            query //= 2
            flipped_nodes[query] = not flipped_nodes.get(query, False)

    count = 0
    for value in flipped_nodes.values():
        if value:
            count += 1

    return count
```

## Test Case 1

### Modified Program

```py
def flip_trees(n, queries):
    flipped_nodes = {}
    for query in queries:
        flipped_nodes[query] = not flipped_nodes.get(query, False)
        while query > 1:
            query //= 2
            flipped_nodes[query] = not flipped_nodes.get(query, False)
    count = 0
    for value in flipped_nodes.values():
        if value:
            count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def flip_trees(n, queries):\n    flipped_nodes = {}\n    for query in queries:\n        flipped_nodes[query] = not flipped_nodes.get(query, False)\n        while query > 1:\n            query //= 2\n            flipped_nodes[query] = not flipped_nodes.get(query, False)\n    count = 0\n    for value in flipped_nodes.values():\n        if value:\n            count += 1\n    return count"
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
        "flip_trees": {
            "name": "flip_trees",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "n",
                    "val1": "*",
                    "valueArray": [
                        "n",
                        "*"
                    ],
                    "valueList": [
                        "n",
                        "*"
                    ]
                },
                {
                    "val0": "queries",
                    "val1": "*",
                    "valueArray": [
                        "queries",
                        "*"
                    ],
                    "valueList": [
                        "queries",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "DictInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "queries",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "queries",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "queries",
                                "primed": false,
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
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "values",
                            "args": [
                                {
                                    "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                        "val0": "query",
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
                            "query",
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
                            "query",
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
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "query",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "query",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "8": [
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
                "9": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "value",
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
                            "value",
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
                            "value",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "value",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
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
                "3": {
                    "true": 8
                },
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
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {},
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'flip_trees'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'while' loop at line 5",
                "6": "*after* the 'while' loop starting at line 5",
                "7": "inside the body of the 'while' loop beginning at line 6",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "query": "*",
                "count": "*",
                "iter#1": "int",
                "iter#0": "int",
                "value": "*",
                "flipped_nodes": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def flip_trees(var_0, var_1):
    flipped_nodes = {}
    for query in var_1:
        flipped_nodes[query] = not flipped_nodes.get(query, False)
        while query > 1:
            query //= 2
            flipped_nodes[query] = not flipped_nodes.get(query, False)
    count = 0
    for value in flipped_nodes.values():
        if value:
            count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def flip_trees(var_0, var_1):\n    flipped_nodes = {}\n    for query in var_1:\n        flipped_nodes[query] = not flipped_nodes.get(query, False)\n        while query > 1:\n            query //= 2\n            flipped_nodes[query] = not flipped_nodes.get(query, False)\n    count = 0\n    for value in flipped_nodes.values():\n        if value:\n            count += 1\n    return count"
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
        "flip_trees": {
            "name": "flip_trees",
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
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "DictInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
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
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "values",
                            "args": [
                                {
                                    "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                        "val0": "query",
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
                            "query",
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
                            "query",
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
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "query",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "query",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "8": [
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
                "9": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "value",
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
                            "value",
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
                            "value",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "value",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
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
                "3": {
                    "true": 8
                },
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
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {},
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'flip_trees'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'while' loop at line 5",
                "6": "*after* the 'while' loop starting at line 5",
                "7": "inside the body of the 'while' loop beginning at line 6",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "query": "*",
                "count": "*",
                "iter#1": "int",
                "iter#0": "int",
                "value": "*",
                "flipped_nodes": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def flip_trees(var_2, var_3):
    flipped_nodes = {}
    for query in var_3:
        flipped_nodes[query] = not flipped_nodes.get(query, False)
        while query > 1:
            query //= 2
            flipped_nodes[query] = not flipped_nodes.get(query, False)
    count = 0
    for value in flipped_nodes.values():
        if value:
            count += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def flip_trees(var_2, var_3):\n    flipped_nodes = {}\n    for query in var_3:\n        flipped_nodes[query] = not flipped_nodes.get(query, False)\n        while query > 1:\n            query //= 2\n            flipped_nodes[query] = not flipped_nodes.get(query, False)\n    count = 0\n    for value in flipped_nodes.values():\n        if value:\n            count += 1\n    return count"
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
        "flip_trees": {
            "name": "flip_trees",
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
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "DictInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "flipped_nodes",
                            {
                                "name": "DictInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_3",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
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
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "values",
                            "args": [
                                {
                                    "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                                "name": "values",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
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
                        "val0": "query",
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
                            "query",
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
                            "query",
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
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "query",
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
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "query",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "query",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "query",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "query",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "flipped_nodes",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "flipped_nodes",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "query",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "get",
                                            "args": [
                                                {
                                                    "name": "flipped_nodes",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "query",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                            "flipped_nodes",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "flipped_nodes",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "query",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "get",
                                                "args": [
                                                    {
                                                        "name": "flipped_nodes",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "query",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "False",
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
                    }
                ],
                "8": [
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
                "9": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "value",
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
                            "value",
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
                            "value",
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
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "value",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "count",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "value",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "count",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
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
                "3": {
                    "true": 8
                },
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
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {},
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'flip_trees'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'while' loop at line 5",
                "6": "*after* the 'while' loop starting at line 5",
                "7": "inside the body of the 'while' loop beginning at line 6",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "query": "*",
                "count": "*",
                "iter#1": "int",
                "iter#0": "int",
                "value": "*",
                "flipped_nodes": "*"
            }
        }
    }
}
```

</details>

