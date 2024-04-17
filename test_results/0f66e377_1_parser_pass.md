# Test Report

Time: 2024-04-14 07:00:08.250564

### Base Program

```py
def product_of_even_numbers(n):
    product = 1
    for i in range(2, n+1, 2):
        product *= i
    return product
```

## Test Case 1

### Modified Program

```py
def product_of_even_numbers(n):
    product = 1
    for i in range(2, n + 1, 2):
        product *= i
    return product
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def product_of_even_numbers(n):\n    product = 1\n    for i in range(2, n + 1, 2):\n        product *= i\n    return product"
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
        "product_of_even_numbers": {
            "name": "product_of_even_numbers",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "product",
                        "val1": {
                            "value": "1",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "product",
                            {
                                "value": "1",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "value": "1",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "2",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
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
                                {
                                    "value": "2",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "2",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    {
                                        "value": "2",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "2",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
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
                                    {
                                        "value": "2",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
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
                        "val0": "$ret",
                        "val1": {
                            "name": "product",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "i",
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
                            "i",
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
                            "i",
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
                        "val0": "product",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "product",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "product",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "product",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                "1": "around the beginning of function 'product_of_even_numbers'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "product": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>
