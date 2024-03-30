# Test Report

Time: 2024-03-30 07:57:35.663710

### Base Program

```py
def concatenationValue(nums):
    value = 0
    while nums:
        n = len(nums)
        if n == 1:
            value += nums[0]
            nums.pop()
        else:
            value += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop()
    return value
```

## Test Case 1

### Modified Program

```py
def concatenationValue(nums):
    value = 0
    while nums:
        n = len(nums)
        if n == 1:
            value += nums[0]
            nums.pop()
        else:
            value += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop()
    return value
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def concatenationValue(nums):\n    value = 0\n    while nums:\n        n = len(nums)\n        if n == 1:\n            value += nums[0]\n            nums.pop()\n        else:\n            value += int(str(nums[0]) + str(nums[-1]))\n            nums.pop(0)\n            nums.pop()\n    return value"
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
        "concatenationValue": {
            "name": "concatenationValue",
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
                        "val0": "value",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "value",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "nums",
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
                                        "name": "nums",
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
                                        "name": "nums",
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
                        "val0": "value",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "nums",
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
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "nums",
                                                                            "primed": false,
                                                                            "line": 9,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "USub",
                                                                            "args": [
                                                                                {
                                                                                    "value": "1",
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
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
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
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
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
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "nums",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pop",
                                                            "args": [
                                                                {
                                                                    "name": "nums",
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
                                                            "value": "0",
                                                            "line": 10,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "nums",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
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
                "1": "around the beginning of function 'concatenationValue'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "value": "*",
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
def concatenationValue(var_0):
    value = 0
    while var_0:
        n = len(var_0)
        if n == 1:
            value += var_0[0]
            var_0.pop()
        else:
            value += int(str(var_0[0]) + str(var_0[-1]))
            var_0.pop(0)
            var_0.pop()
    return value
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def concatenationValue(var_0):\n    value = 0\n    while var_0:\n        n = len(var_0)\n        if n == 1:\n            value += var_0[0]\n            var_0.pop()\n        else:\n            value += int(str(var_0[0]) + str(var_0[-1]))\n            var_0.pop(0)\n            var_0.pop()\n    return value"
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
        "concatenationValue": {
            "name": "concatenationValue",
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
                        "val0": "value",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "var_0",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "value",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
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
                        "val0": "value",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "var_0",
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
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "var_0",
                                                                            "primed": false,
                                                                            "line": 9,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "USub",
                                                                            "args": [
                                                                                {
                                                                                    "value": "1",
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
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_0",
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
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_0",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_0",
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
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_0",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "var_0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
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
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pop",
                                                            "args": [
                                                                {
                                                                    "name": "var_0",
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
                                                            "value": "0",
                                                            "line": 10,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
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
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "var_0",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
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
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "var_0",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
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
                "1": "around the beginning of function 'concatenationValue'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "value": "*",
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
def concatenationValue(nums):
    value = 0
    while nums:
        n = len(nums)
        if n == 1:
            value += nums[0]
            nums.pop()
        else:
            value += int(str(nums[-1]) + str(nums[0]))
            nums.pop(0)
            nums.pop()
    return value
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def concatenationValue(nums):\n    value = 0\n    while nums:\n        n = len(nums)\n        if n == 1:\n            value += nums[0]\n            nums.pop()\n        else:\n            value += int(str(nums[-1]) + str(nums[0]))\n            nums.pop(0)\n            nums.pop()\n    return value"
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
        "concatenationValue": {
            "name": "concatenationValue",
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
                        "val0": "value",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "value",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "nums",
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
                                        "name": "nums",
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
                                        "name": "nums",
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
                        "val0": "value",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "nums",
                                                                            "primed": false,
                                                                            "line": 9,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "USub",
                                                                            "args": [
                                                                                {
                                                                                    "value": "1",
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
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "nums",
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
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
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
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "nums",
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
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "nums",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "nums",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pop",
                                                            "args": [
                                                                {
                                                                    "name": "nums",
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
                                                            "value": "0",
                                                            "line": 10,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "nums",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "nums",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "nums",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
                                                                "args": [
                                                                    {
                                                                        "name": "nums",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
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
                "1": "around the beginning of function 'concatenationValue'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "value": "*",
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
def concatenationValue(var_1):
    value = 0
    while var_1:
        n = len(var_1)
        if n == 1:
            value += var_1[0]
            var_1.pop()
        else:
            value += int(str(var_1[-1]) + str(var_1[0]))
            var_1.pop(0)
            var_1.pop()
    return value
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def concatenationValue(var_1):\n    value = 0\n    while var_1:\n        n = len(var_1)\n        if n == 1:\n            value += var_1[0]\n            var_1.pop()\n        else:\n            value += int(str(var_1[-1]) + str(var_1[0]))\n            var_1.pop(0)\n            var_1.pop()\n    return value"
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
        "concatenationValue": {
            "name": "concatenationValue",
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
                        "val0": "value",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "value",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "value",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
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
                        "val0": "value",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
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
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "value",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "var_1",
                                                                            "primed": false,
                                                                            "line": 9,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "USub",
                                                                            "args": [
                                                                                {
                                                                                    "value": "1",
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
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "str",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "var_1",
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
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_1",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_1",
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
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "value",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
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
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "value",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_1",
                                                                                "primed": false,
                                                                                "line": 9,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "USub",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "1",
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
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "str",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "var_1",
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
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "var_1",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": true,
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
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
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
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "pop",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "pop",
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
                                                            "value": "0",
                                                            "line": 10,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
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
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_1",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
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
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": true,
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
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
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
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "pop",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "pop",
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
                                                                "value": "0",
                                                                "line": 10,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
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
                                "line": 5
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
                "1": "around the beginning of function 'concatenationValue'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "value": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

