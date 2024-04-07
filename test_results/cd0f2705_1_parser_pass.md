# Test Report

Time: 2024-04-07 08:15:15.211450

### Base Program

```py
def main(x):
	return x
```

## Test Case 1

### Modified Program

```py
def main(x):
	x = x + 0
	x = x + 0
	x = x + 0
	x = x + 0
	x = x + 0
	return x
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(x):\n\tx = x + 0\n\tx = x + 0\n\tx = x + 0\n\tx = x + 0\n\tx = x + 0\n\treturn x"
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
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
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
                                                                    "value": "0",
                                                                    "line": 2,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 2,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 3,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 3,
                                                    "tokentype": "Operation"
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
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
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
                                                                        "value": "0",
                                                                        "line": 2,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 2,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 3,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 3,
                                                        "tokentype": "Operation"
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
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
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
                                                                        "value": "0",
                                                                        "line": 2,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 2,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 3,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 3,
                                                        "tokentype": "Operation"
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
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "x",
                            "primed": true,
                            "line": 7,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": true,
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": true,
                                "line": 7
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'main'"
            },
            "types": {
                "x": "*"
            }
        }
    }
}
```

</details>

