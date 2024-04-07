# Test Report

Time: 2024-04-07 07:43:45.648395

### Base Program

```py
def main(p):
	p = p + 5
	return p
```

## Test Case 1

### Modified Program

```py
def main(p):
	p = p + 5
	p = p - 5
	p = p + 5
	return p
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(p):\n\tp = p + 5\n\tp = p - 5\n\tp = p + 5\n\treturn p"
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
                    "val0": "p",
                    "val1": "*",
                    "valueArray": [
                        "p",
                        "*"
                    ],
                    "valueList": [
                        "p",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "p",
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
                                            "value": "5",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
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
                        "valueArray": [
                            "p",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "p",
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
                                                "value": "5",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "5",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "p",
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
                                                "value": "5",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "5",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "p",
                            "primed": true,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "p",
                                "primed": true,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "p",
                                "primed": true,
                                "line": 5
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
                "p": "*"
            }
        }
    }
}
```

</details>

