# Test Report

Time: 2024-04-14 11:24:03.248225

### Base Program

```py
def maxTurbulenceSize(arr):
    n = len(arr)
    result = 1
    i = 0

    while i < n - 1:
        if arr[i] == arr[i + 1]:
            i += 1
            continue

        j = i + 1
        while j < n - 1 and ((arr[j] > arr[j + 1]) != (arr[j - 1] > arr[j])):
            j += 1
        
        result = max(result, j - i + 1)
        i = j

    return result
```

## Test Case 1

### Modified Program

```py
def maxTurbulenceSize(arr):
    n = len(arr)
    result = 1
    i = 0
    while i < n - 1:
        if arr[i] == arr[i + 1]:
            i += 1
            continue
        j = i + 1
        while j < n - 1 and (arr[j] > arr[j + 1]) != (arr[j - 1] > arr[j]):
            j += 1
        result = max(result, j - i + 1)
        i = j
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTurbulenceSize(arr):\n    n = len(arr)\n    result = 1\n    i = 0\n    while i < n - 1:\n        if arr[i] == arr[i + 1]:\n            i += 1\n            continue\n        j = i + 1\n        while j < n - 1 and (arr[j] > arr[j + 1]) != (arr[j - 1] > arr[j]):\n            j += 1\n        result = max(result, j - i + 1)\n        i = j\n    return result"
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
        "maxTurbulenceSize": {
            "name": "maxTurbulenceSize",
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
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
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
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
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
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "n",
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    }
                                ],
                                "line": 5
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
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "i",
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
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
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
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
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
                "6": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                        "val0": "j",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "i",
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
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "9": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "j",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "n",
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
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
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
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "j",
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
                                            "name": "Gt",
                                            "args": [
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
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "j",
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
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
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "j",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "11": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "j",
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
                        "valueArray": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                "3": {},
                "4": {
                    "true": 5
                },
                "5": {
                    "false": 8,
                    "true": 6
                },
                "6": {
                    "true": 2
                },
                "8": {
                    "true": 9
                },
                "9": {
                    "false": 10,
                    "true": 11
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 9
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTurbulenceSize'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "8": "after the if-statement beginning at line 6",
                "9": "the condition of the 'while' loop at line 10",
                "10": "*after* the 'while' loop starting at line 10",
                "11": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "result": "*",
                "i": "*",
                "j": "*",
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
def maxTurbulenceSize(var_16):
    n = len(var_16)
    result = 1
    i = 0
    while i < n - 1:
        if var_16[i] == var_16[i + 1]:
            i += 1
            continue
        j = i + 1
        while j < n - 1 and (var_16[j] > var_16[j + 1]) != (var_16[j - 1] > var_16[j]):
            j += 1
        result = max(result, j - i + 1)
        i = j
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTurbulenceSize(var_16):\n    n = len(var_16)\n    result = 1\n    i = 0\n    while i < n - 1:\n        if var_16[i] == var_16[i + 1]:\n            i += 1\n            continue\n        j = i + 1\n        while j < n - 1 and (var_16[j] > var_16[j + 1]) != (var_16[j - 1] > var_16[j]):\n            j += 1\n        result = max(result, j - i + 1)\n        i = j\n    return result"
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
        "maxTurbulenceSize": {
            "name": "maxTurbulenceSize",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_16",
                    "val1": "*",
                    "valueArray": [
                        "var_16",
                        "*"
                    ],
                    "valueList": [
                        "var_16",
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
                                    "name": "var_16",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_16",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_16",
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
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "n",
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    }
                                ],
                                "line": 5
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
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_16",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_16",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "i",
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
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_16",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_16",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
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
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_16",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_16",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
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
                "6": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                        "val0": "j",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "i",
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
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                    }
                ],
                "9": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "j",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "n",
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
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_16",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_16",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "j",
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
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_16",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "j",
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_16",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "n",
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_16",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
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
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "j",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "11": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "j",
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
                        "valueArray": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                "3": {},
                "4": {
                    "true": 5
                },
                "5": {
                    "false": 8,
                    "true": 6
                },
                "6": {
                    "true": 2
                },
                "8": {
                    "true": 9
                },
                "9": {
                    "false": 10,
                    "true": 11
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 9
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTurbulenceSize'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "8": "after the if-statement beginning at line 6",
                "9": "the condition of the 'while' loop at line 10",
                "10": "*after* the 'while' loop starting at line 10",
                "11": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "result": "*",
                "i": "*",
                "j": "*",
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
def maxTurbulenceSize(arr):
    n = len(arr)
    result = 1
    i = 0
    while i < n + -1:
        if arr[i] == arr[1 + i]:
            i += 1
            continue
        j = 1 + i
        while j < n + -1 and (arr[j] > arr[1 + j]) != (arr[j + -1] > arr[j]):
            j += 1
        result = max(result, 1 + (j + -i))
        i = j
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTurbulenceSize(arr):\n    n = len(arr)\n    result = 1\n    i = 0\n    while i < n + -1:\n        if arr[i] == arr[1 + i]:\n            i += 1\n            continue\n        j = 1 + i\n        while j < n + -1 and (arr[j] > arr[1 + j]) != (arr[j + -1] > arr[j]):\n            j += 1\n        result = max(result, 1 + (j + -i))\n        i = j\n    return result"
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
        "maxTurbulenceSize": {
            "name": "maxTurbulenceSize",
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
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
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
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
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
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
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
                                    }
                                ],
                                "line": 5
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
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "arr",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "i",
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
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "i",
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
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "arr",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "i",
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
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                        "val0": "j",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "j",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "n",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
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
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
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
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "value": "1",
                                                                    "line": 10,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                        {
                                            "name": "Gt",
                                            "args": [
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
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "j",
                                                                    "primed": false,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "value": "1",
                                                                        "line": 10,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "value": "1",
                                                                        "line": 10,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                            {
                                                "name": "Gt",
                                                "args": [
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
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 12,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 12,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 12,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 12,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 12,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 12,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 12,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "j",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "11": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "j",
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
                        "valueArray": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                "3": {},
                "4": {
                    "true": 5
                },
                "5": {
                    "false": 8,
                    "true": 6
                },
                "6": {
                    "true": 2
                },
                "8": {
                    "true": 9
                },
                "9": {
                    "false": 10,
                    "true": 11
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 9
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTurbulenceSize'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "8": "after the if-statement beginning at line 6",
                "9": "the condition of the 'while' loop at line 10",
                "10": "*after* the 'while' loop starting at line 10",
                "11": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "result": "*",
                "i": "*",
                "j": "*",
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
def maxTurbulenceSize(var_17):
    n = len(var_17)
    result = 1
    i = 0
    while i < n + -1:
        if var_17[i] == var_17[1 + i]:
            i += 1
            continue
        j = 1 + i
        while j < n + -1 and (var_17[j] > var_17[1 + j]) != (var_17[j + -1] > var_17[j]):
            j += 1
        result = max(result, 1 + (j + -i))
        i = j
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxTurbulenceSize(var_17):\n    n = len(var_17)\n    result = 1\n    i = 0\n    while i < n + -1:\n        if var_17[i] == var_17[1 + i]:\n            i += 1\n            continue\n        j = 1 + i\n        while j < n + -1 and (var_17[j] > var_17[1 + j]) != (var_17[j + -1] > var_17[j]):\n            j += 1\n        result = max(result, 1 + (j + -i))\n        i = j\n    return result"
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
        "maxTurbulenceSize": {
            "name": "maxTurbulenceSize",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_17",
                    "val1": "*",
                    "valueArray": [
                        "var_17",
                        "*"
                    ],
                    "valueList": [
                        "var_17",
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
                                    "name": "var_17",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_17",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_17",
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
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
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
                                    }
                                ],
                                "line": 5
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
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 14
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_17",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_17",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "i",
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
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_17",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_17",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "i",
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
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_17",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_17",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "i",
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
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
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
                        "val0": "j",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 9,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "j",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "n",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
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
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_17",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_17",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
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
                                                                    "name": "j",
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
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_17",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "j",
                                                                    "primed": false,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_17",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
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
                                                                        "name": "j",
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
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "j",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
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
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
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
                                                                        "name": "j",
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
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "j",
                                                                        "primed": false,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_17",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 12,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "j",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 12,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 12,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 12,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 12,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 12,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "j",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 12,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "j",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "j",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "11": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "j",
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
                        "valueArray": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "j",
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
                "3": {},
                "4": {
                    "true": 5
                },
                "5": {
                    "false": 8,
                    "true": 6
                },
                "6": {
                    "true": 2
                },
                "8": {
                    "true": 9
                },
                "9": {
                    "false": 10,
                    "true": 11
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 9
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'maxTurbulenceSize'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "8": "after the if-statement beginning at line 6",
                "9": "the condition of the 'while' loop at line 10",
                "10": "*after* the 'while' loop starting at line 10",
                "11": "inside the body of the 'while' loop beginning at line 11"
            },
            "types": {
                "result": "*",
                "i": "*",
                "j": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

