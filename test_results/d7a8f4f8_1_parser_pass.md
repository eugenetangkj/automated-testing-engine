# Test Report

Time: 2024-04-06 13:48:53.289515

### Base Program

```py
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

## Test Case 1

### Modified Program

```py
def test_function(a, b, c, d):
    c = (a if a > 5 else b) + (c if c < 10 else d)
    return c
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function(a, b, c, d):\n    c = (a if a > 5 else b) + (c if c < 10 else d)\n    return c"
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
                },
                {
                    "val0": "d",
                    "val1": "*",
                    "valueArray": [
                        "d",
                        "*"
                    ],
                    "valueList": [
                        "d",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "c",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ite",
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
                                                    "value": "5",
                                                    "line": 2,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "b",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "c",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "10",
                                                    "line": 2,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "c",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "d",
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
                        },
                        "valueArray": [
                            "c",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ite",
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
                                                        "value": "5",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "c",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "10",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "c",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "d",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
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
                            "c",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ite",
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
                                                        "value": "5",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "c",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "10",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "c",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "d",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "c",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "c",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "c",
                                "primed": true,
                                "line": 3
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
            "types": {
                "c": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def test_function(a, b, c, d):
    if a > 5 and c < 10:
        c = a + c
    elif a > 5 and (not c < 10):
        c = a + d
    elif not a > 5 and c < 10:
        c = b + c
    elif not a > 5 and (not c < 10):
        c = b + d
    return c
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function(a, b, c, d):\n    if a > 5 and c < 10:\n        c = a + c\n    elif a > 5 and (not c < 10):\n        c = a + d\n    elif not a > 5 and c < 10:\n        c = b + c\n    elif not a > 5 and (not c < 10):\n        c = b + d\n    return c"
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
                },
                {
                    "val0": "d",
                    "val1": "*",
                    "valueArray": [
                        "d",
                        "*"
                    ],
                    "valueList": [
                        "d",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "c",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
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
                                                    "value": "5",
                                                    "line": 2,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "c",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "10",
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
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "c",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "Gt",
                                                    "args": [
                                                        {
                                                            "name": "a",
                                                            "primed": false,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "5",
                                                            "line": 4,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "Lt",
                                                            "args": [
                                                                {
                                                                    "name": "c",
                                                                    "primed": false,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "10",
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
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "a",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "d",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "ite",
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
                                                                            "line": 6,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "value": "5",
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
                                                            "name": "Lt",
                                                            "args": [
                                                                {
                                                                    "name": "c",
                                                                    "primed": false,
                                                                    "line": 6,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "10",
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
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "b",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "c",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 7,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "ite",
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
                                                                                    "line": 8,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "value": "5",
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
                                                                {
                                                                    "name": "Not",
                                                                    "args": [
                                                                        {
                                                                            "name": "Lt",
                                                                            "args": [
                                                                                {
                                                                                    "name": "c",
                                                                                    "primed": false,
                                                                                    "line": 8,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "value": "10",
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
                                                                }
                                                            ],
                                                            "line": 8,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "b",
                                                                    "primed": false,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "d",
                                                                    "primed": false,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "c",
                                                            "primed": false,
                                                            "line": 0,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 8,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "c",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
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
                                                        "value": "5",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "c",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "10",
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
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "c",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Gt",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "5",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "Lt",
                                                                "args": [
                                                                    {
                                                                        "name": "c",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "10",
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
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "d",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "ite",
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
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "5",
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
                                                                "name": "Lt",
                                                                "args": [
                                                                    {
                                                                        "name": "c",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "10",
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
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
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
                                                                                        "line": 8,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "value": "5",
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
                                                                    {
                                                                        "name": "Not",
                                                                        "args": [
                                                                            {
                                                                                "name": "Lt",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "c",
                                                                                        "primed": false,
                                                                                        "line": 8,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "value": "10",
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
                                                                    }
                                                                ],
                                                                "line": 8,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "b",
                                                                        "primed": false,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "d",
                                                                        "primed": false,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 0,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "c",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
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
                                                        "value": "5",
                                                        "line": 2,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "c",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "10",
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
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "c",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Gt",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "5",
                                                                "line": 4,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "Lt",
                                                                "args": [
                                                                    {
                                                                        "name": "c",
                                                                        "primed": false,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "10",
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
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "d",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "ite",
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
                                                                                "line": 6,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "value": "5",
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
                                                                "name": "Lt",
                                                                "args": [
                                                                    {
                                                                        "name": "c",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "10",
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
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ite",
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
                                                                                        "line": 8,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "value": "5",
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
                                                                    {
                                                                        "name": "Not",
                                                                        "args": [
                                                                            {
                                                                                "name": "Lt",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "c",
                                                                                        "primed": false,
                                                                                        "line": 8,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "value": "10",
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
                                                                    }
                                                                ],
                                                                "line": 8,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "b",
                                                                        "primed": false,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "d",
                                                                        "primed": false,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "c",
                                                                "primed": false,
                                                                "line": 0,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "c",
                            "primed": true,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "c",
                                "primed": true,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "c",
                                "primed": true,
                                "line": 10
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
            "types": {
                "c": "*"
            }
        }
    }
}
```

</details>

