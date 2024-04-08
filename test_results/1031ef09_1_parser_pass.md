# Test Report

Time: 2024-04-08 07:09:47.613610

### Base Program

```py
def main():
	my_list = []
	if not my_list:
		return 1
	else:
		return 0
```

## Test Case 1

### Modified Program

```py
def main():
	my_list = []
	if not my_list:
		return 1
	else:
		return 0
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\tmy_list = []\n\tif not my_list:\n\t\treturn 1\n\telse:\n\t\treturn 0"
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
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "my_list",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "my_list",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "my_list",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "my_list",
                                            "primed": true,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "my_list",
                                                "primed": true,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "my_list",
                                                "primed": true,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
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
                "my_list": "*"
            }
        }
    }
}
```

</details>

