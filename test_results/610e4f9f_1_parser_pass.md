# Test Report

Time: 2024-04-14 07:36:04.266325

### Base Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

## Test Case 1

### Modified Program

```py
def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def calculate_bmi(weight, height):\n    bmi = weight / height ** 2\n    return bmi"
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
        "calculate_bmi": {
            "name": "calculate_bmi",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "weight",
                    "val1": "*",
                    "valueArray": [
                        "weight",
                        "*"
                    ],
                    "valueList": [
                        "weight",
                        "*"
                    ]
                },
                {
                    "val0": "height",
                    "val1": "*",
                    "valueArray": [
                        "height",
                        "*"
                    ],
                    "valueList": [
                        "height",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "bmi",
                        "val1": {
                            "name": "Div",
                            "args": [
                                {
                                    "name": "weight",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "name": "height",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "2",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "bmi",
                            {
                                "name": "Div",
                                "args": [
                                    {
                                        "name": "weight",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "height",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "bmi",
                            {
                                "name": "Div",
                                "args": [
                                    {
                                        "name": "weight",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "height",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "bmi",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "bmi",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "bmi",
                                "primed": true,
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
                "1": "around the beginning of function 'calculate_bmi'"
            },
            "types": {
                "bmi": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def calculate_bmi(weight, height):
    if True:
        bmi = weight / height ** 2
        return bmi
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def calculate_bmi(weight, height):\n    if True:\n        bmi = weight / height ** 2\n        return bmi"
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
        "calculate_bmi": {
            "name": "calculate_bmi",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "weight",
                    "val1": "*",
                    "valueArray": [
                        "weight",
                        "*"
                    ],
                    "valueList": [
                        "weight",
                        "*"
                    ]
                },
                {
                    "val0": "height",
                    "val1": "*",
                    "valueArray": [
                        "height",
                        "*"
                    ],
                    "valueList": [
                        "height",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "bmi",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "value": "True",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Div",
                                    "args": [
                                        {
                                            "name": "weight",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Pow",
                                            "args": [
                                                {
                                                    "name": "height",
                                                    "primed": false,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "2",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "bmi",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "bmi",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Div",
                                        "args": [
                                            {
                                                "name": "weight",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "height",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "bmi",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "bmi",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Div",
                                        "args": [
                                            {
                                                "name": "weight",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "height",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "bmi",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
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
                                    "value": "True",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Div",
                                    "args": [
                                        {
                                            "name": "weight",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Pow",
                                            "args": [
                                                {
                                                    "name": "height",
                                                    "primed": false,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "2",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
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
                                        "name": "Div",
                                        "args": [
                                            {
                                                "name": "weight",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "height",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
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
                                        "name": "Div",
                                        "args": [
                                            {
                                                "name": "weight",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "height",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
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
                "1": "around the beginning of function 'calculate_bmi'"
            },
            "types": {
                "bmi": "*"
            }
        }
    }
}
```

</details>

