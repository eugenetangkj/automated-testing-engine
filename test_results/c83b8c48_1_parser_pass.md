# Test Report

Time: 2024-04-02 07:29:14.282901

### Base Program

```py
def multiply_two_numbers(a, b):
	product = a * b
	return product
```

## Test Case 1

### Modified Program

```py
def multiply_two_numbers(a, b):
    product = a * b
    return product
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_two_numbers(a, b):\n    product = a * b\n    return product"
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
        "multiply_two_numbers": {
            "name": "multiply_two_numbers",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "product",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "b",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
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
                            "name": "product",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "product",
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
                "1": "around the beginning of function 'multiply_two_numbers'"
            },
            "types": {
                "product": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def multiply_two_numbers(var_0, var_1):
    product = var_0 * var_1
    return product
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_two_numbers(var_0, var_1):\n    product = var_0 * var_1\n    return product"
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
        "multiply_two_numbers": {
            "name": "multiply_two_numbers",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_0",
                    "val1": "*",
                    "valueArray": [
                        "var_0",
                        "*"
                    ],
                    "valueList": [
                        "var_0",
                        "*"
                    ]
                },
                {
                    "val0": "var_1",
                    "val1": "*",
                    "valueArray": [
                        "var_1",
                        "*"
                    ],
                    "valueList": [
                        "var_1",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "product",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 2,
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
                            "name": "product",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "product",
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
                "1": "around the beginning of function 'multiply_two_numbers'"
            },
            "types": {
                "product": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def multiply_two_numbers(a, b):
    product = b * a
    return product
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_two_numbers(a, b):\n    product = b * a\n    return product"
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
        "multiply_two_numbers": {
            "name": "multiply_two_numbers",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "product",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "b",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
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
                            "name": "product",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "product",
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
                "1": "around the beginning of function 'multiply_two_numbers'"
            },
            "types": {
                "product": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def multiply_two_numbers(var_2, var_3):
    product = var_3 * var_2
    return product
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_two_numbers(var_2, var_3):\n    product = var_3 * var_2\n    return product"
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
        "multiply_two_numbers": {
            "name": "multiply_two_numbers",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_2",
                    "val1": "*",
                    "valueArray": [
                        "var_2",
                        "*"
                    ],
                    "valueList": [
                        "var_2",
                        "*"
                    ]
                },
                {
                    "val0": "var_3",
                    "val1": "*",
                    "valueArray": [
                        "var_3",
                        "*"
                    ],
                    "valueList": [
                        "var_3",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "product",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "product",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 2,
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
                            "name": "product",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "product",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "product",
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
                "1": "around the beginning of function 'multiply_two_numbers'"
            },
            "types": {
                "product": "*"
            }
        }
    }
}
```

</details>

