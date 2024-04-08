# Test Report

Time: 2024-04-07 07:40:14.194472

### Base Program

```py
def main(v):
	v = v + 5
	return v
```

## Test Case 1

### Modified Program

```py
def main(v):
	v = v + 5
	v = v
	return v
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main(v):\n\tv = v + 5\n\tv = v\n\treturn v"
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
                    "val0": "v",
                    "val1": "*",
                    "valueArray": [
                        "v",
                        "*"
                    ],
                    "valueList": [
                        "v",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "v",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "v",
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
                            "v",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "v",
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
                            "v",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "v",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "v",
                            "primed": true,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "v",
                                "primed": true,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "v",
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
                "v": "*"
            }
        }
    }
}
```

</details>

