# Test Report

Time: 2024-04-07 07:22:18.643856

### Base Program

```py
def main(x):
	x = x + 5
	return x
```

## Test Case 1

### Modified Program

```py
def main(x):
	x = x + 5
	for j in range(2, 5):
		x += 0
	return x
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(x):\n\tx = x + 5\n\tfor j in range(2, 5):\n\t\tx += 0\n\treturn x"
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
        "main": {
            "name": "main",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "x",
                    "val1": "*",
                    "valueArray": [
                        "x",
                        "*"
                    ],
                    "valueList": [
                        "x",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "x",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "x",
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
                        "valueArray": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "x",
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
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "x",
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
                                    "value": "5",
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
                                        "value": "5",
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
                                        "value": "5",
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
                            "name": "x",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": false,
                                "line": 5
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
                            "j",
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
                            "j",
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
                        "val0": "x",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "x",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "x",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "x",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'main'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ind#0": "int",
                "x": "*",
                "iter#0": "int",
                "j": "*"
            }
        }
    }
}
```

</details>

