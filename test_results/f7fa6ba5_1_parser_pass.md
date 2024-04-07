# Test Report

Time: 2024-04-07 09:24:36.219320

### Base Program

```py
def main(a, b):
	diff = a - b
	return diff
```

## Test Case 1

### Modified Program

```py
def main(a, b):
	a, b = b, a
	diff = b - a
	return diff
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(a, b):\n\ta, b = b, a\n\tdiff = b - a\n\treturn diff"
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "b",
                        "val1": {
                            "name": "a",
                            "primed": false,
                            "line": 2,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "b",
                            {
                                "name": "a",
                                "primed": false,
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "name": "a",
                                "primed": false,
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "b",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "diff",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "diff",
                            "primed": true,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "diff",
                                "primed": true,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "diff",
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
                "b": "*",
                "diff": "*"
            }
        }
    }
}
```

</details>

