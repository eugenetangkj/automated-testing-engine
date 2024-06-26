# Test Report

Time: 2024-04-14 07:33:15.772359

### Base Program

```py
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

## Test Case 1

### Modified Program

```py
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def calculate_circle_area(radius):\n    return 3.14159 * radius * radius"
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
        "calculate_circle_area": {
            "name": "calculate_circle_area",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "radius",
                    "val1": "*",
                    "valueArray": [
                        "radius",
                        "*"
                    ],
                    "valueList": [
                        "radius",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "value": "3.14159",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "radius",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "radius",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "value": "3.14159",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "radius",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "radius",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "value": "3.14159",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "radius",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "radius",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
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
                "1": "around the beginning of function 'calculate_circle_area'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def calculate_circle_area(radius):
    if True:
        return 3.14159 * radius * radius
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def calculate_circle_area(radius):\n    if True:\n        return 3.14159 * radius * radius"
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
        "calculate_circle_area": {
            "name": "calculate_circle_area",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "radius",
                    "val1": "*",
                    "valueArray": [
                        "radius",
                        "*"
                    ],
                    "valueList": [
                        "radius",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "value": "True",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "value": "3.14159",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "radius",
                                                    "primed": false,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "radius",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "value": "3.14159",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "radius",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "radius",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "value": "3.14159",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "radius",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "radius",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
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
                "1": "around the beginning of function 'calculate_circle_area'"
            },
            "types": {}
        }
    }
}
```

</details>

