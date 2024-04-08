# Test Report

Time: 2024-04-08 08:52:33.248022

### Base Program

```py
def func():
	return 100
```

## Test Case 1

### Modified Program

```py
def func():
    return 100
```

<details>
<summary>repair endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"100\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"100\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"100\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"100\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\"}, \"types\": {}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
[
    {
        "totalCost": 0.0,
        "localRepairs": []
    }
]
```

</details>

## Test Case 2

### Modified Program

```py
def func():
    try:
        return 100
    except:
        return 1
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"100\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"100\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"1\", \"line\": 5}], \"valueList\": [\"$ret\", {\"value\": \"1\", \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\"}, \"types\": {}}}}",
    "function": "func",
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
        "totalCost": 2.0,
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
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "$ret",
                        "primed": false,
                        "line": 0
                    },
                    "val1": {
                        "tokentype": "Constant",
                        "value": "1",
                        "line": 5
                    },
                    "val2": {
                        "tokentype": "Constant",
                        "value": "100",
                        "line": 2
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
                            "value": "1",
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "100",
                            "line": 2
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
                            "value": "1",
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "100",
                            "line": 2
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
                "funcName": "func"
            }
        ]
    }
]
```

</details>

