# Test Report

Time: 2024-04-07 07:37:25.897538

### Base Program

```py
def main(z):
	z = z + 5
	return z
```

## Test Case 1

### Modified Program

```py
def main(z):
	z = z + 5
	x = z
	return z
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(z):\n\tz = z + 5\n\tx = z\n\treturn z"
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
                    "val0": "z",
                    "val1": "*",
                    "valueArray": [
                        "z",
                        "*"
                    ],
                    "valueList": [
                        "z",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "z",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "z",
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
                            "z",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "z",
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
                            "z",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "z",
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
                            "name": "z",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "z",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "z",
                                "primed": true,
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "z",
                            "primed": true,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "z",
                                "primed": true,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "z",
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
                "z": "*"
            }
        }
    }
}
```

</details>

