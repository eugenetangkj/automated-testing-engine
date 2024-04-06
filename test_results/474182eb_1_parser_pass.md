# Test Report

Time: 2024-04-06 10:22:25.108153

### Base Program

```py
def main():
	 return {'key1': 1, 'key2': 2 }
```

## Test Case 1

### Modified Program

```py
def main():
	 return {'key1': 1, 'key2': 2 
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\t return {'key1': 1, 'key2': 2 "
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
                        "val0": "$ret",
                        "val1": {
                            "name": "DictInit",
                            "args": [
                                {
                                    "value": "\"key1\"",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "1",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "\"key2\"",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "DictInit",
                                "args": [
                                    {
                                        "value": "\"key1\"",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "1",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "\"key2\"",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "DictInit",
                                "args": [
                                    {
                                        "value": "\"key1\"",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "1",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "\"key2\"",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'main'"
            },
            "types": {}
        }
    }
}
```

</details>

