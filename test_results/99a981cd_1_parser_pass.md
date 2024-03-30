# Test Report

Time: 2024-03-30 08:32:19.851343

### Base Program

```py
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

## Test Case 1

### Modified Program

```py
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def containsDuplicate(nums):\n    return len(nums) != len(set(nums))"
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
        "containsDuplicate": {
            "name": "containsDuplicate",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "NotEq",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "set",
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
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'containsDuplicate'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def containsDuplicate(var_0):
    return len(var_0) != len(set(var_0))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def containsDuplicate(var_0):\n    return len(var_0) != len(set(var_0))"
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
        "containsDuplicate": {
            "name": "containsDuplicate",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "NotEq",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "set",
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
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'containsDuplicate'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def containsDuplicate(var_1):
    return len(var_1) != len(set(var_1))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def containsDuplicate(var_1):\n    return len(var_1) != len(set(var_1))"
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
        "containsDuplicate": {
            "name": "containsDuplicate",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "NotEq",
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
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "set",
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
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "NotEq",
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
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "set",
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
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'containsDuplicate'"
            },
            "types": {}
        }
    }
}
```

</details>

