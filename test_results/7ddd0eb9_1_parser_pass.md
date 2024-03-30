# Test Report

Time: 2024-03-30 06:25:32.438855

### Base Program

```py
from sortedcontainers import SortedList

def advantage_count(nums1, nums2):
    nums1_sorted = SortedList(nums1)
    result = []
    for num in nums2:
        index = nums1_sorted.bisect_right(num)
        if index == len(nums1_sorted):
            val = nums1_sorted.pop(0)
        else:
            val = nums1_sorted.pop(index)
        result.append(val)
    return result
```

## Test Case 1

### Modified Program

```py
from sortedcontainers import SortedList

def advantage_count(nums1, nums2):
    nums1_sorted = SortedList(nums1)
    result = []
    for num in nums2:
        index = nums1_sorted.bisect_right(num)
        if index == len(nums1_sorted):
            val = nums1_sorted.pop(0)
        else:
            val = nums1_sorted.pop(index)
        result.append(val)
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from sortedcontainers import SortedList\n\ndef advantage_count(nums1, nums2):\n    nums1_sorted = SortedList(nums1)\n    result = []\n    for num in nums2:\n        index = nums1_sorted.bisect_right(num)\n        if index == len(nums1_sorted):\n            val = nums1_sorted.pop(0)\n        else:\n            val = nums1_sorted.pop(index)\n        result.append(val)\n    return result"
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
        "from sortedcontainers import SortedList"
    ],
    "fncs": {
        "advantage_count": {
            "name": "advantage_count",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "nums1",
                    "val1": "*",
                    "valueArray": [
                        "nums1",
                        "*"
                    ],
                    "valueList": [
                        "nums1",
                        "*"
                    ]
                },
                {
                    "val0": "nums2",
                    "val1": "*",
                    "valueArray": [
                        "nums2",
                        "*"
                    ],
                    "valueList": [
                        "nums2",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "SortedList",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "nums1",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1",
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
                        "val0": "result",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "nums2",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "nums2",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "nums2",
                                "primed": false,
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
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_right",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "nums1_sorted",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "num",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
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
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                        },
                                        {
                                            "value": "0",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "val",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
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
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "val",
                                    "primed": true,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                "1": "around the beginning of function 'advantage_count'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "result": "*",
                "val": "*",
                "ind#0": "int",
                "num": "*",
                "index": "*",
                "iter#0": "int",
                "nums1_sorted": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
from sortedcontainers import SortedList

def advantage_count(var_0, var_1):
    nums1_sorted = SortedList(var_0)
    result = []
    for num in var_1:
        index = nums1_sorted.bisect_right(num)
        if index == len(nums1_sorted):
            val = nums1_sorted.pop(0)
        else:
            val = nums1_sorted.pop(index)
        result.append(val)
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from sortedcontainers import SortedList\n\ndef advantage_count(var_0, var_1):\n    nums1_sorted = SortedList(var_0)\n    result = []\n    for num in var_1:\n        index = nums1_sorted.bisect_right(num)\n        if index == len(nums1_sorted):\n            val = nums1_sorted.pop(0)\n        else:\n            val = nums1_sorted.pop(index)\n        result.append(val)\n    return result"
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
        "from sortedcontainers import SortedList"
    ],
    "fncs": {
        "advantage_count": {
            "name": "advantage_count",
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
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "SortedList",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
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
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
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
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
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
                        "val0": "result",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
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
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_right",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "nums1_sorted",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "num",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
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
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                        },
                                        {
                                            "value": "0",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "val",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
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
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "val",
                                    "primed": true,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                "1": "around the beginning of function 'advantage_count'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "result": "*",
                "val": "*",
                "ind#0": "int",
                "num": "*",
                "index": "*",
                "iter#0": "int",
                "nums1_sorted": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
from sortedcontainers import SortedList

def advantage_count(var_2, var_3):
    nums1_sorted = SortedList(var_2)
    result = []
    for num in var_3:
        index = nums1_sorted.bisect_right(num)
        if index == len(nums1_sorted):
            val = nums1_sorted.pop(0)
        else:
            val = nums1_sorted.pop(index)
        result.append(val)
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from sortedcontainers import SortedList\n\ndef advantage_count(var_2, var_3):\n    nums1_sorted = SortedList(var_2)\n    result = []\n    for num in var_3:\n        index = nums1_sorted.bisect_right(num)\n        if index == len(nums1_sorted):\n            val = nums1_sorted.pop(0)\n        else:\n            val = nums1_sorted.pop(index)\n        result.append(val)\n    return result"
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
        "from sortedcontainers import SortedList"
    ],
    "fncs": {
        "advantage_count": {
            "name": "advantage_count",
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
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "SortedList",
                                    "line": 4,
                                    "tokentype": "Constant"
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
                        },
                        "valueArray": [
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
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
                            "nums1_sorted",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "SortedList",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
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
                        "val0": "result",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_3",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
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
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                    },
                    {
                        "val0": "index",
                        "val1": {
                            "name": "FuncCall",
                            "args": [
                                {
                                    "value": "bisect_right",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "nums1_sorted",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "num",
                                    "primed": true,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
                                        "primed": true,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "index",
                            {
                                "name": "FuncCall",
                                "args": [
                                    {
                                        "value": "bisect_right",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "nums1_sorted",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "num",
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
                        "val0": "nums1_sorted",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                        },
                                        {
                                            "value": "0",
                                            "line": 9,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "nums1_sorted",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                            },
                                            {
                                                "value": "0",
                                                "line": 9,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "val",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "index",
                                            "primed": true,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums1_sorted",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "index",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
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
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "val",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "index",
                                                "primed": true,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums1_sorted",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "index",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "name": "append",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "val",
                                    "primed": true,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "append",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "val",
                                        "primed": true,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                "1": "around the beginning of function 'advantage_count'",
                "2": "the condition of the 'for' loop at line 6",
                "3": "*after* the 'for' loop starting at line 6",
                "4": "inside the body of the 'for' loop beginning at line 7"
            },
            "types": {
                "result": "*",
                "val": "*",
                "ind#0": "int",
                "num": "*",
                "index": "*",
                "iter#0": "int",
                "nums1_sorted": "*"
            }
        }
    }
}
```

</details>

