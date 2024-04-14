# Test Report

Time: 2024-04-14 07:37:31.807331

### Base Program

```py
def product_of_two_numbers(x, y):
	return x * y
```

## Test Case 1

### Modified Program

```py
def product_of_two_numbers(x, y):
    return x * y
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def product_of_two_numbers(x, y):\n    return x * y"
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
        "product_of_two_numbers": {
            "name": "product_of_two_numbers",
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
                },
                {
                    "val0": "y",
                    "val1": "*",
                    "valueArray": [
                        "y",
                        "*"
                    ],
                    "valueList": [
                        "y",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "x",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "y",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "x",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "y",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "x",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "y",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
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
                "1": "around the beginning of function 'product_of_two_numbers'"
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
def product_of_two_numbers(x, y):
    if True:
        return x * y
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def product_of_two_numbers(x, y):\n    if True:\n        return x * y"
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
        "product_of_two_numbers": {
            "name": "product_of_two_numbers",
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
                },
                {
                    "val0": "y",
                    "val1": "*",
                    "valueArray": [
                        "y",
                        "*"
                    ],
                    "valueList": [
                        "y",
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
                                    "value": "True",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "y",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
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
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "y",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
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
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "y",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
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
                "1": "around the beginning of function 'product_of_two_numbers'"
            },
            "types": {}
        }
    }
}
```

</details>

