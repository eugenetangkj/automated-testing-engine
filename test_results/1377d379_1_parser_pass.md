# Test Report

Time: 2024-04-07 07:30:59.031510

### Base Program

```py
def main(y):
	y = y + 5
	return y
```

## Test Case 1

### Modified Program

```py
def main(y):
	y = y + 5
	x = y
	return x
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(y):\n\ty = y + 5\n\tx = y\n\treturn x"
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
                        "val0": "y",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "y",
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
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "y",
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
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "y",
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
                        "val0": "x",
                        "val1": {
                            "name": "y",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "y",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "y",
                                "primed": true,
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "x",
                            "primed": true,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": true,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": true,
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
                "1": "around the beginning of function 'main'"
            },
            "types": {
                "x": "*",
                "y": "*"
            }
        }
    }
}
```

</details>

