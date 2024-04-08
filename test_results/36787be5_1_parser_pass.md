# Test Report

Time: 2024-04-07 15:52:25.432222

### Base Program

```py
def main(g, h):
	diff = g - h
	return diff
```

## Test Case 1

### Modified Program

```py
def main(g, h):
	g, h = h, g
	diff = h - g
	return diff
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(g, h):\n\tg, h = h, g\n\tdiff = h - g\n\treturn diff"
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
                    "val0": "g",
                    "val1": "*",
                    "valueArray": [
                        "g",
                        "*"
                    ],
                    "valueList": [
                        "g",
                        "*"
                    ]
                },
                {
                    "val0": "h",
                    "val1": "*",
                    "valueArray": [
                        "h",
                        "*"
                    ],
                    "valueList": [
                        "h",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "h",
                        "val1": {
                            "name": "g",
                            "primed": false,
                            "line": 2,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "h",
                            {
                                "name": "g",
                                "primed": false,
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "h",
                            {
                                "name": "g",
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
                                    "name": "h",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "g",
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
                                        "name": "h",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "g",
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
                                        "name": "h",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "g",
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
                "h": "*",
                "diff": "*"
            }
        }
    }
}
```

</details>

