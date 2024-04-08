# Test Report

Time: 2024-04-06 15:16:45.901321

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
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "function": "test_string",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Repair endpoint failed
```

Actual Output: 
```json
[
    {
        "totalCost": 34.0,
        "localRepairs": [
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 34.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "$ret",
                        "primed": false,
                        "line": 0
                    },
                    "val1": {
                        "tokentype": "Operation",
                        "name": "Add",
                        "args": [
                            {
                                "tokentype": "Operation",
                                "name": "Add",
                                "args": [
                                    {
                                        "tokentype": "Constant",
                                        "value": "\"Part 1\"",
                                        "line": 2
                                    },
                                    {
                                        "tokentype": "Constant",
                                        "value": "\"Part 2\"",
                                        "line": 2
                                    }
                                ],
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "\"Part 3\"",
                                "line": 2
                            }
                        ],
                        "line": 2
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "DictInit",
                        "args": [],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Add",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "Add",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 1\"",
                                            "line": 2
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 2\"",
                                            "line": 2
                                        }
                                    ],
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "\"Part 3\"",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "DictInit",
                            "args": [],
                            "line": 0
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Add",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "Add",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 1\"",
                                            "line": 2
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 2\"",
                                            "line": 2
                                        }
                                    ],
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "\"Part 3\"",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "DictInit",
                            "args": [],
                            "line": 0
                        }
                    ]
                },
                "errorLocation": {
                    "val0": 1,
                    "val1": 1,
                    "valueArray": [
                        1,
                        1
                    ],
                    "valueList": [
                        1,
                        1
                    ]
                },
                "funcName": "test_string"
            }
        ]
    }
]
```

</details>

