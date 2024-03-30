# Test Report

Time: 2024-03-30 08:34:03.387698

### Base Program

```py
from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [jobs[0][2]]
    
    def latestNonConflict(index):
        startTimeToFind = jobs[index][1]
        index = bisect_left([job[0] for job in jobs], startTimeToFind)
        if index:
            return index - 1
        return -1

    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))

    return dp[-1]
```

## Test Case 1

### Modified Program

```py
from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [jobs[0][2]]

    def latestNonConflict(index):
        startTimeToFind = jobs[index][1]
        index = bisect_left([job[0] for job in jobs], startTimeToFind)
        if index:
            return index - 1
        return -1
    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from bisect import bisect_left\n\ndef jobScheduling(startTime, endTime, profit):\n    jobs = sorted(zip(endTime, startTime, profit))\n    dp = [jobs[0][2]]\n\n    def latestNonConflict(index):\n        startTimeToFind = jobs[index][1]\n        index = bisect_left([job[0] for job in jobs], startTimeToFind)\n        if index:\n            return index - 1\n        return -1\n    for i in range(1, len(jobs)):\n        L = latestNonConflict(i)\n        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))\n    return dp[-1]"
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
        "from bisect import bisect_left"
    ],
    "fncs": {
        "jobScheduling": {
            "name": "jobScheduling",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "startTime",
                    "val1": "*",
                    "valueArray": [
                        "startTime",
                        "*"
                    ],
                    "valueList": [
                        "startTime",
                        "*"
                    ]
                },
                {
                    "val0": "endTime",
                    "val1": "*",
                    "valueArray": [
                        "endTime",
                        "*"
                    ],
                    "valueList": [
                        "endTime",
                        "*"
                    ]
                },
                {
                    "val0": "profit",
                    "val1": "*",
                    "valueArray": [
                        "profit",
                        "*"
                    ],
                    "valueList": [
                        "profit",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "jobs",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "zip",
                                    "args": [
                                        {
                                            "name": "endTime",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "startTime",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "profit",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "endTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "startTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "profit",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "endTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "startTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "profit",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                        "val0": "dp",
                        "val1": {
                            "name": "ListInit",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "jobs",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 5,
                                            "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'jobScheduling'"
            },
            "types": {
                "jobs": "*",
                "dp": "*"
            }
        },
        "latestNonConflict": {
            "name": "latestNonConflict",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "index",
                    "val1": "*",
                    "valueArray": [
                        "index",
                        "*"
                    ],
                    "valueList": [
                        "index",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "startTimeToFind",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "jobs",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_left",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "job",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 9,
                                                    "tokentype": "Constant"
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
                                    "name": "startTimeToFind",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 13,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
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
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
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
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
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
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
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
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
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
                                "line": 10
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
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
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
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "L",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "latestNonConflict",
                                    "line": 14,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 14,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "dp",
                                                    "primed": false,
                                                    "line": 15,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 15,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 15,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "dp",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "jobs",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 5
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'latestNonConflict'",
                "5": "the condition of the 'for' loop at line 13",
                "6": "*after* the 'for' loop starting at line 13",
                "7": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "startTimeToFind": "*",
                "ind#0": "int",
                "index": "*",
                "i": "*",
                "iter#0": "int",
                "L": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
from bisect import bisect_left

def jobScheduling(var_0, var_1, var_2):
    jobs = sorted(zip(var_1, var_0, var_2))
    dp = [jobs[0][2]]

    def latestNonConflict(var_3):
        startTimeToFind = jobs[var_3][1]
        var_3 = bisect_left([job[0] for job in jobs], startTimeToFind)
        if var_3:
            return var_3 - 1
        return -1
    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from bisect import bisect_left\n\ndef jobScheduling(var_0, var_1, var_2):\n    jobs = sorted(zip(var_1, var_0, var_2))\n    dp = [jobs[0][2]]\n\n    def latestNonConflict(var_3):\n        startTimeToFind = jobs[var_3][1]\n        var_3 = bisect_left([job[0] for job in jobs], startTimeToFind)\n        if var_3:\n            return var_3 - 1\n        return -1\n    for i in range(1, len(jobs)):\n        L = latestNonConflict(i)\n        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))\n    return dp[-1]"
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
        "from bisect import bisect_left"
    ],
    "fncs": {
        "jobScheduling": {
            "name": "jobScheduling",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "jobs",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "zip",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_2",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                        "val0": "dp",
                        "val1": {
                            "name": "ListInit",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "jobs",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 5,
                                            "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'jobScheduling'"
            },
            "types": {
                "jobs": "*",
                "dp": "*"
            }
        },
        "latestNonConflict": {
            "name": "latestNonConflict",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
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
                        "val0": "startTimeToFind",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "jobs",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                        "val0": "var_3",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_left",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "job",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 9,
                                                    "tokentype": "Constant"
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
                                    "name": "startTimeToFind",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_3",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "var_3",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 13,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "var_3",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "var_3",
                                            "primed": true,
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
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "var_3",
                                                "primed": true,
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "var_3",
                                                "primed": true,
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
                                "line": 10
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
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
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
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "L",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "latestNonConflict",
                                    "line": 14,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 14,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "dp",
                                                    "primed": false,
                                                    "line": 15,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 15,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 15,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "dp",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "jobs",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 5
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'latestNonConflict'",
                "5": "the condition of the 'for' loop at line 13",
                "6": "*after* the 'for' loop starting at line 13",
                "7": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "startTimeToFind": "*",
                "var_3": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "L": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [jobs[0][2]]

    def latestNonConflict(index):
        startTimeToFind = jobs[index][1]
        index = bisect_left([job[0] for job in jobs], startTimeToFind)
        if index:
            return index + -1
        return -1
    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], jobs[i][2] + (0 if L == -1 else dp[L])))
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from bisect import bisect_left\n\ndef jobScheduling(startTime, endTime, profit):\n    jobs = sorted(zip(endTime, startTime, profit))\n    dp = [jobs[0][2]]\n\n    def latestNonConflict(index):\n        startTimeToFind = jobs[index][1]\n        index = bisect_left([job[0] for job in jobs], startTimeToFind)\n        if index:\n            return index + -1\n        return -1\n    for i in range(1, len(jobs)):\n        L = latestNonConflict(i)\n        dp.append(max(dp[-1], jobs[i][2] + (0 if L == -1 else dp[L])))\n    return dp[-1]"
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
        "from bisect import bisect_left"
    ],
    "fncs": {
        "jobScheduling": {
            "name": "jobScheduling",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "startTime",
                    "val1": "*",
                    "valueArray": [
                        "startTime",
                        "*"
                    ],
                    "valueList": [
                        "startTime",
                        "*"
                    ]
                },
                {
                    "val0": "endTime",
                    "val1": "*",
                    "valueArray": [
                        "endTime",
                        "*"
                    ],
                    "valueList": [
                        "endTime",
                        "*"
                    ]
                },
                {
                    "val0": "profit",
                    "val1": "*",
                    "valueArray": [
                        "profit",
                        "*"
                    ],
                    "valueList": [
                        "profit",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "jobs",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "zip",
                                    "args": [
                                        {
                                            "name": "endTime",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "startTime",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "profit",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "endTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "startTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "profit",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "endTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "startTime",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "profit",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                        "val0": "dp",
                        "val1": {
                            "name": "ListInit",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "jobs",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 5,
                                            "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'jobScheduling'"
            },
            "types": {
                "jobs": "*",
                "dp": "*"
            }
        },
        "latestNonConflict": {
            "name": "latestNonConflict",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "index",
                    "val1": "*",
                    "valueArray": [
                        "index",
                        "*"
                    ],
                    "valueList": [
                        "index",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "startTimeToFind",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "jobs",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "index",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "index",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_left",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "job",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 9,
                                                    "tokentype": "Constant"
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
                                    "name": "startTimeToFind",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 13,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "index",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
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
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
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
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
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
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "index",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
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
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                "line": 10
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
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
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
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "L",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "latestNonConflict",
                                    "line": 14,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 14,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "dp",
                                                    "primed": false,
                                                    "line": 15,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "jobs",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 15,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 15,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "dp",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 5
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'latestNonConflict'",
                "5": "the condition of the 'for' loop at line 13",
                "6": "*after* the 'for' loop starting at line 13",
                "7": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "startTimeToFind": "*",
                "ind#0": "int",
                "index": "*",
                "i": "*",
                "iter#0": "int",
                "L": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
from bisect import bisect_left

def jobScheduling(var_4, var_5, var_6):
    jobs = sorted(zip(var_5, var_4, var_6))
    dp = [jobs[0][2]]

    def latestNonConflict(var_7):
        startTimeToFind = jobs[var_7][1]
        var_7 = bisect_left([job[0] for job in jobs], startTimeToFind)
        if var_7:
            return var_7 + -1
        return -1
    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], jobs[i][2] + (0 if L == -1 else dp[L])))
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from bisect import bisect_left\n\ndef jobScheduling(var_4, var_5, var_6):\n    jobs = sorted(zip(var_5, var_4, var_6))\n    dp = [jobs[0][2]]\n\n    def latestNonConflict(var_7):\n        startTimeToFind = jobs[var_7][1]\n        var_7 = bisect_left([job[0] for job in jobs], startTimeToFind)\n        if var_7:\n            return var_7 + -1\n        return -1\n    for i in range(1, len(jobs)):\n        L = latestNonConflict(i)\n        dp.append(max(dp[-1], jobs[i][2] + (0 if L == -1 else dp[L])))\n    return dp[-1]"
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
        "from bisect import bisect_left"
    ],
    "fncs": {
        "jobScheduling": {
            "name": "jobScheduling",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "jobs",
                        "val1": {
                            "name": "sorted",
                            "args": [
                                {
                                    "name": "zip",
                                    "args": [
                                        {
                                            "name": "var_5",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_4",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_6",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_6",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "jobs",
                            {
                                "name": "sorted",
                                "args": [
                                    {
                                        "name": "zip",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_6",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                        "val0": "dp",
                        "val1": {
                            "name": "ListInit",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "jobs",
                                                    "primed": true,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 5,
                                            "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                            "dp",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "jobs",
                                                        "primed": true,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 5,
                                                "tokentype": "Constant"
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'jobScheduling'"
            },
            "types": {
                "jobs": "*",
                "dp": "*"
            }
        },
        "latestNonConflict": {
            "name": "latestNonConflict",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "startTimeToFind",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "jobs",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_7",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_7",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                            "startTimeToFind",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "jobs",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_7",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
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
                        "val0": "var_7",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_left",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "job",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 9,
                                                    "tokentype": "Constant"
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
                                    "name": "startTimeToFind",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_7",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "var_7",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_left",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "job",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 9,
                                                        "tokentype": "Constant"
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
                                        "name": "startTimeToFind",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 13,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "jobs",
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 13,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 13
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "var_7",
                                    "primed": true,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "var_7",
                                            "primed": true,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
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
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "var_7",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_7",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "var_7",
                                        "primed": true,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_7",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                "line": 10
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
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 16,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 16,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 16
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
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
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
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                        "val0": "L",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "latestNonConflict",
                                    "line": 14,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 14,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 14,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "L",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "latestNonConflict",
                                        "line": 14,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 14,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 14
                            }
                        ]
                    },
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "max",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "dp",
                                                    "primed": false,
                                                    "line": 15,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "jobs",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 15,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 15,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 15,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "dp",
                                                                    "primed": false,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "L",
                                                                    "primed": true,
                                                                    "line": 15,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 15,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 15,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 15,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "max",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "dp",
                                                        "primed": false,
                                                        "line": 15,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "jobs",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 15,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 15,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 15,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "dp",
                                                                        "primed": false,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "L",
                                                                        "primed": true,
                                                                        "line": 15,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 15,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 15,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 15,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 5
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'latestNonConflict'",
                "5": "the condition of the 'for' loop at line 13",
                "6": "*after* the 'for' loop starting at line 13",
                "7": "inside the body of the 'for' loop beginning at line 14"
            },
            "types": {
                "var_7": "*",
                "startTimeToFind": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int",
                "L": "*"
            }
        }
    }
}
```

</details>

