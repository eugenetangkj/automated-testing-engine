# Test Report

Time: 2024-04-08 07:48:55.847768

### Base Program

```py
def main():
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

## Test Case 1

### Modified Program

```py
def main():
	curr_string = 'Hello World'
	try:
		index = curr_string.index('Hello')
		return True
	except ValueError:
		return False
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"False\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"False\", \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
    "function": "main",
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
                            "name": "curr_string",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "curr_string",
                            "primed": true,
                            "line": 0
                        }
                    ],
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
                        "tokentype": "Constant",
                        "value": "False",
                        "line": 7
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "ite",
                        "args": [
                            {
                                "tokentype": "Operation",
                                "name": "In",
                                "args": [
                                    {
                                        "tokentype": "Constant",
                                        "value": "\"Hello\"",
                                        "line": 3
                                    },
                                    {
                                        "tokentype": "Variable",
                                        "name": "curr_string",
                                        "primed": true,
                                        "line": 0
                                    }
                                ],
                                "line": 0
                            },
                            {
                                "tokentype": "Constant",
                                "value": "True",
                                "line": 4
                            },
                            {
                                "tokentype": "Constant",
                                "value": "False",
                                "line": 5
                            }
                        ],
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
                            "tokentype": "Constant",
                            "value": "False",
                            "line": 7
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ite",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "In",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Hello\"",
                                            "line": 3
                                        },
                                        {
                                            "tokentype": "Variable",
                                            "name": "curr_string",
                                            "primed": true,
                                            "line": 0
                                        }
                                    ],
                                    "line": 0
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "True",
                                    "line": 4
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "False",
                                    "line": 5
                                }
                            ],
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
                            "tokentype": "Constant",
                            "value": "False",
                            "line": 7
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ite",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "In",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Hello\"",
                                            "line": 3
                                        },
                                        {
                                            "tokentype": "Variable",
                                            "name": "curr_string",
                                            "primed": true,
                                            "line": 0
                                        }
                                    ],
                                    "line": 0
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "True",
                                    "line": 4
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "False",
                                    "line": 5
                                }
                            ],
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
                "funcName": "main"
            }
        ]
    }
]
```

</details>

