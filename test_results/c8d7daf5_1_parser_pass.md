# Test Report

Time: 2024-04-06 15:16:37.939018

### Base Program

```py
def test_string():
	return ('Part 1'
	'Part 2'
	'Part 3')
```

## Test Case 1

### Modified Program

```py
def test_string():
	return 'Part 1' + 'Part 2' + 'Part 3'
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_string():\n\treturn 'Part 1' + 'Part 2' + 'Part 3'"
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
        "test_string": {
            "name": "test_string",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "\"Part 1\"",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "\"Part 2\"",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "\"Part 3\"",
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
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "\"Part 1\"",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "\"Part 2\"",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "\"Part 3\"",
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
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "\"Part 1\"",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "\"Part 2\"",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "\"Part 3\"",
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
                "1": "around the beginning of function 'test_string'"
            },
            "types": {}
        }
    }
}
```

</details>

