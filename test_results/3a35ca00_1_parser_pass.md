# Test Report

Time: 2024-03-30 07:53:40.823027

### Base Program

```py
def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])
```

## Test Case 1

### Modified Program

```py
def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_partition_difference(nums):\n    n = len(nums) // 2\n    nums.sort(reverse=True)\n    return sum(nums[:n]) - sum(nums[n:])"
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
        "min_partition_difference": {
            "name": "min_partition_difference",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "nums",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "nums",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "nums",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "nums",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_partition_difference'"
            },
            "types": {
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
def min_partition_difference(var_0):
    n = len(var_0) // 2
    var_0.sort(reverse=True)
    return sum(var_0[:n]) - sum(var_0[n:])
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_partition_difference(var_0):\n    n = len(var_0) // 2\n    var_0.sort(reverse=True)\n    return sum(var_0[:n]) - sum(var_0[n:])"
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
        "min_partition_difference": {
            "name": "min_partition_difference",
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
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "len",
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
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
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
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
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
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
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
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
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
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "value": "None",
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
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_partition_difference'"
            },
            "types": {
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
def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) + -sum(nums[n:])
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_partition_difference(nums):\n    n = len(nums) // 2\n    nums.sort(reverse=True)\n    return sum(nums[:n]) + -sum(nums[n:])"
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
        "min_partition_difference": {
            "name": "min_partition_difference",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "nums",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "nums",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "nums",
                        "val1": {
                            "name": "sort",
                            "args": [
                                {
                                    "name": "nums",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "nums",
                            {
                                "name": "sort",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "sum",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "nums",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "name": "n",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "None",
                                                                    "line": 4,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "None",
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
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "sum",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "name": "n",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "sum",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "nums",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "name": "n",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_partition_difference'"
            },
            "types": {
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
def min_partition_difference(var_1):
    n = len(var_1) // 2
    var_1.sort(reverse=True)
    return sum(var_1[:n]) + -sum(var_1[n:])
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_partition_difference(var_1):\n    n = len(var_1) // 2\n    var_1.sort(reverse=True)\n    return sum(var_1[:n]) + -sum(var_1[n:])"
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
        "min_partition_difference": {
            "name": "min_partition_difference",
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
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
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
                                },
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
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
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
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
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "sum",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Slice",
                                                    "args": [
                                                        {
                                                            "value": "None",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "n",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "None",
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
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "sum",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Slice",
                                                            "args": [
                                                                {
                                                                    "name": "n",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "None",
                                                                    "line": 4,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "None",
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
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "sum",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "name": "n",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "sum",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Slice",
                                                        "args": [
                                                            {
                                                                "value": "None",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "n",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "None",
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
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "sum",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Slice",
                                                                "args": [
                                                                    {
                                                                        "name": "n",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "None",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "None",
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_partition_difference'"
            },
            "types": {
                "n": "*"
            }
        }
    }
}
```

</details>

