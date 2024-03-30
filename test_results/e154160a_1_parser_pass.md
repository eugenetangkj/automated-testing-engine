# Test Report

Time: 2024-03-30 06:30:10.857319

### Base Program

```py
def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt
```

## Test Case 1

### Modified Program

```py
def maxTasks(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()
    cnt = 0
    i = 0
    for j in range(pills):
        while i < len(tasks) and tasks[i] > workers[j] + strength:
            i += 1
        if i < len(tasks):
            cnt += 1
            i += 1
    i = 0
    for j in range(pills, len(workers)):
        if i < len(tasks) and tasks[i] <= workers[j]:
            cnt += 1
            i += 1
    return cnt
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTasks(tasks, workers, pills, strength):\n    tasks.sort()\n    workers.sort()\n    cnt = 0\n    i = 0\n    for j in range(pills):\n        while i < len(tasks) and tasks[i] > workers[j] + strength:\n            i += 1\n        if i < len(tasks):\n            cnt += 1\n            i += 1\n    i = 0\n    for j in range(pills, len(workers)):\n        if i < len(tasks) and tasks[i] <= workers[j]:\n            cnt += 1\n            i += 1\n    return cnt"
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
        "maxTasks": {
            "name": "maxTasks",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "tasks",
                    "val1": "*",
                    "valueArray": [
                        "tasks",
                        "*"
                    ],
                    "valueList": [
                        "tasks",
                        "*"
                    ]
                },
                {
                    "val0": "workers",
                    "val1": "*",
                    "valueArray": [
                        "workers",
                        "*"
                    ],
                    "valueList": [
                        "workers",
                        "*"
                    ]
                },
                {
                    "val0": "pills",
                    "val1": "*",
                    "valueArray": [
                        "pills",
                        "*"
                    ],
                    "valueList": [
                        "pills",
                        "*"
                    ]
                },
                {
                    "val0": "strength",
                    "val1": "*",
                    "valueArray": [
                        "strength",
                        "*"
                    ],
                    "valueList": [
                        "strength",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "tasks",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "tasks",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "tasks",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "tasks",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "tasks",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "tasks",
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
                        "val0": "workers",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "workers",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "workers",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "workers",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "workers",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "workers",
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
                        "val0": "cnt",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
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
                                    "name": "pills",
                                    "primed": false,
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
                                        "name": "pills",
                                        "primed": false,
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
                                        "name": "pills",
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
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 12,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "pills",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "workers",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "pills",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "workers",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "pills",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "workers",
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
                "4": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 7,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "strength",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "strength",
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
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "strength",
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
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
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
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
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
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "11": [
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
                "12": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "cnt",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "13": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                    },
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
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
                    "true": 11
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
                "11": {
                    "false": 12,
                    "true": 13
                },
                "12": {},
                "13": {
                    "true": 11
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTasks'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8",
                "11": "the condition of the 'for' loop at line 13",
                "12": "*after* the 'for' loop starting at line 13",
                "13": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "cnt": "*",
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
def maxTasks(var_0, var_1, var_2, var_3):
    var_0.sort()
    var_1.sort()
    cnt = 0
    i = 0
    for j in range(var_2):
        while i < len(var_0) and var_0[i] > var_1[j] + var_3:
            i += 1
        if i < len(var_0):
            cnt += 1
            i += 1
    i = 0
    for j in range(var_2, len(var_1)):
        if i < len(var_0) and var_0[i] <= var_1[j]:
            cnt += 1
            i += 1
    return cnt
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTasks(var_0, var_1, var_2, var_3):\n    var_0.sort()\n    var_1.sort()\n    cnt = 0\n    i = 0\n    for j in range(var_2):\n        while i < len(var_0) and var_0[i] > var_1[j] + var_3:\n            i += 1\n        if i < len(var_0):\n            cnt += 1\n            i += 1\n    i = 0\n    for j in range(var_2, len(var_1)):\n        if i < len(var_0) and var_0[i] <= var_1[j]:\n            cnt += 1\n            i += 1\n    return cnt"
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
        "maxTasks": {
            "name": "maxTasks",
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
                },
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
                        "val0": "var_0",
                        "val1": {
                            "name": "sort",
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
                            "var_0",
                            {
                                "name": "sort",
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
                            "var_0",
                            {
                                "name": "sort",
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
                        "val0": "var_1",
                        "val1": {
                            "name": "sort",
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
                        "valueArray": [
                            "var_1",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "cnt",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
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
                                    "name": "var_2",
                                    "primed": false,
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
                                        "name": "var_2",
                                        "primed": false,
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
                                        "name": "var_2",
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
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 12,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_1",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
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
                "4": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
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
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Gt",
                                    "args": [
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
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
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
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
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
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Gt",
                                        "args": [
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
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
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
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
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
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "11": [
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
                "12": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "cnt",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "13": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                    },
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
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
                    "true": 11
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
                "11": {
                    "false": 12,
                    "true": 13
                },
                "12": {},
                "13": {
                    "true": 11
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTasks'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8",
                "11": "the condition of the 'for' loop at line 13",
                "12": "*after* the 'for' loop starting at line 13",
                "13": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "cnt": "*",
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
def maxTasks(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()
    cnt = 0
    i = 0
    for j in range(pills):
        while i < len(tasks) and tasks[i] > strength + workers[j]:
            i += 1
        if i < len(tasks):
            cnt += 1
            i += 1
    i = 0
    for j in range(pills, len(workers)):
        if i < len(tasks) and tasks[i] <= workers[j]:
            cnt += 1
            i += 1
    return cnt
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTasks(tasks, workers, pills, strength):\n    tasks.sort()\n    workers.sort()\n    cnt = 0\n    i = 0\n    for j in range(pills):\n        while i < len(tasks) and tasks[i] > strength + workers[j]:\n            i += 1\n        if i < len(tasks):\n            cnt += 1\n            i += 1\n    i = 0\n    for j in range(pills, len(workers)):\n        if i < len(tasks) and tasks[i] <= workers[j]:\n            cnt += 1\n            i += 1\n    return cnt"
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
        "maxTasks": {
            "name": "maxTasks",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "tasks",
                    "val1": "*",
                    "valueArray": [
                        "tasks",
                        "*"
                    ],
                    "valueList": [
                        "tasks",
                        "*"
                    ]
                },
                {
                    "val0": "workers",
                    "val1": "*",
                    "valueArray": [
                        "workers",
                        "*"
                    ],
                    "valueList": [
                        "workers",
                        "*"
                    ]
                },
                {
                    "val0": "pills",
                    "val1": "*",
                    "valueArray": [
                        "pills",
                        "*"
                    ],
                    "valueList": [
                        "pills",
                        "*"
                    ]
                },
                {
                    "val0": "strength",
                    "val1": "*",
                    "valueArray": [
                        "strength",
                        "*"
                    ],
                    "valueList": [
                        "strength",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "tasks",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "tasks",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "tasks",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "tasks",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "tasks",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "tasks",
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
                        "val0": "workers",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "workers",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "workers",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "workers",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "workers",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "workers",
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
                        "val0": "cnt",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
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
                                    "name": "pills",
                                    "primed": false,
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
                                        "name": "pills",
                                        "primed": false,
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
                                        "name": "pills",
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
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 12,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "pills",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "workers",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "pills",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "workers",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "pills",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "workers",
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
                "4": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "strength",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "strength",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "strength",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
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
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "tasks",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "tasks",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
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
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "11": [
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
                "12": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "cnt",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "13": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                    },
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "tasks",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "workers",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "tasks",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "workers",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
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
                    "true": 11
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
                "11": {
                    "false": 12,
                    "true": 13
                },
                "12": {},
                "13": {
                    "true": 11
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTasks'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8",
                "11": "the condition of the 'for' loop at line 13",
                "12": "*after* the 'for' loop starting at line 13",
                "13": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "cnt": "*",
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
def maxTasks(var_4, var_5, var_6, var_7):
    var_4.sort()
    var_5.sort()
    cnt = 0
    i = 0
    for j in range(var_6):
        while i < len(var_4) and var_4[i] > var_7 + var_5[j]:
            i += 1
        if i < len(var_4):
            cnt += 1
            i += 1
    i = 0
    for j in range(var_6, len(var_5)):
        if i < len(var_4) and var_4[i] <= var_5[j]:
            cnt += 1
            i += 1
    return cnt
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTasks(var_4, var_5, var_6, var_7):\n    var_4.sort()\n    var_5.sort()\n    cnt = 0\n    i = 0\n    for j in range(var_6):\n        while i < len(var_4) and var_4[i] > var_7 + var_5[j]:\n            i += 1\n        if i < len(var_4):\n            cnt += 1\n            i += 1\n    i = 0\n    for j in range(var_6, len(var_5)):\n        if i < len(var_4) and var_4[i] <= var_5[j]:\n            cnt += 1\n            i += 1\n    return cnt"
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
        "maxTasks": {
            "name": "maxTasks",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
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
                },
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "var_4",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "var_4",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_4",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_4",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "var_4",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_4",
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
                        "val0": "var_5",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "var_5",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_5",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_5",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "var_5",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "var_5",
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
                        "val0": "cnt",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
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
                                    "name": "var_6",
                                    "primed": false,
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
                                        "name": "var_6",
                                        "primed": false,
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
                                        "name": "var_6",
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
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 12,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "var_6",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_5",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_5",
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
                                "name": "range",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_5",
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
                "4": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_4",
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
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_4",
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
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "var_7",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_7",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_7",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_4",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
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
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
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
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_4",
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_4",
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
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
                                        "name": "i",
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
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "11": [
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
                "12": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "cnt",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "cnt",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "13": [
                    {
                        "val0": "j",
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
                            "j",
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
                            "j",
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
                    },
                    {
                        "val0": "cnt",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "cnt",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "cnt",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "cnt",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "cnt",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "cnt",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "len",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "LtE",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 14,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "len",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "LtE",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 14,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
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
                    "true": 11
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
                "11": {
                    "false": 12,
                    "true": 13
                },
                "12": {},
                "13": {
                    "true": 11
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTasks'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7",
                "5": "the condition of the 'while' loop at line 7",
                "6": "*after* the 'while' loop starting at line 7",
                "7": "inside the body of the 'while' loop beginning at line 8",
                "11": "the condition of the 'for' loop at line 13",
                "12": "*after* the 'for' loop starting at line 13",
                "13": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "cnt": "*",
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

