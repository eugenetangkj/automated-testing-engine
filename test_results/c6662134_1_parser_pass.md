# Test Report

Time: 2024-04-06 13:58:38.125698

### Base Program

```py
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function(a, b, c):\n    if a > 100 or (b < 20 and c > 30):\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                },
                {
                    "val0": "c",
                    "val1": "*",
                    "valueArray": [
                        "c",
                        "*"
                    ],
                    "valueList": [
                        "c",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "a",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "100",
                                                    "line": 2,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "b",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "20",
                                                            "line": 2,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Gt",
                                                    "args": [
                                                        {
                                                            "name": "c",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "30",
                                                            "line": 2,
                                                            "tokentype": "Constant"
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
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 5,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "100",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "20",
                                                                "line": 2,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Gt",
                                                        "args": [
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "30",
                                                                "line": 2,
                                                                "tokentype": "Constant"
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
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "100",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "20",
                                                                "line": 2,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Gt",
                                                        "args": [
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "30",
                                                                "line": 2,
                                                                "tokentype": "Constant"
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
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 5,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'test_function'"
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
def test_function(a, b, c):
    if not (not a > 100 and (not (b < 20 and c > 30))):
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function(a, b, c):\n    if not (not a > 100 and (not (b < 20 and c > 30))):\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                },
                {
                    "val0": "c",
                    "val1": "*",
                    "valueArray": [
                        "c",
                        "*"
                    ],
                    "valueList": [
                        "c",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "Gt",
                                                            "args": [
                                                                {
                                                                    "name": "a",
                                                                    "primed": false,
                                                                    "line": 2,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "100",
                                                                    "line": 2,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 2,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "And",
                                                            "args": [
                                                                {
                                                                    "name": "Lt",
                                                                    "args": [
                                                                        {
                                                                            "name": "b",
                                                                            "primed": false,
                                                                            "line": 2,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "value": "20",
                                                                            "line": 2,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 2,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "name": "Gt",
                                                                    "args": [
                                                                        {
                                                                            "name": "c",
                                                                            "primed": false,
                                                                            "line": 2,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "value": "30",
                                                                            "line": 2,
                                                                            "tokentype": "Constant"
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
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 5,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "Gt",
                                                                "args": [
                                                                    {
                                                                        "name": "a",
                                                                        "primed": false,
                                                                        "line": 2,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "100",
                                                                        "line": 2,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 2,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "Lt",
                                                                        "args": [
                                                                            {
                                                                                "name": "b",
                                                                                "primed": false,
                                                                                "line": 2,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "20",
                                                                                "line": 2,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 2,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "Gt",
                                                                        "args": [
                                                                            {
                                                                                "name": "c",
                                                                                "primed": false,
                                                                                "line": 2,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "30",
                                                                                "line": 2,
                                                                                "tokentype": "Constant"
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
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "Gt",
                                                                "args": [
                                                                    {
                                                                        "name": "a",
                                                                        "primed": false,
                                                                        "line": 2,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "100",
                                                                        "line": 2,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 2,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "Lt",
                                                                        "args": [
                                                                            {
                                                                                "name": "b",
                                                                                "primed": false,
                                                                                "line": 2,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "20",
                                                                                "line": 2,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 2,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "Gt",
                                                                        "args": [
                                                                            {
                                                                                "name": "c",
                                                                                "primed": false,
                                                                                "line": 2,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "30",
                                                                                "line": 2,
                                                                                "tokentype": "Constant"
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
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 5,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'test_function'"
            },
            "types": {}
        }
    }
}
```

</details>

