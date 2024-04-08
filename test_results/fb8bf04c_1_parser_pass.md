# Test Report

Time: 2024-04-06 14:53:41.790689

### Base Program

```py
def test_function():
    a = True
    b = False
    if a or b:
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function():
    a = True
    b = False
    if a or b:
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function():\n    a = True\n    b = False\n    if a or b:\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "a",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "b",
                        "val1": {
                            "value": "False",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "b",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
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
                "1": "around the beginning of function 'test_function'"
            },
            "types": {
                "a": "*",
                "b": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def test_function():
    a = True
    b = False
    if a and True or (b and True):
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function():\n    a = True\n    b = False\n    if a and True or (b and True):\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "a",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "b",
                        "val1": {
                            "value": "False",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "a",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "True",
                                                    "line": 4,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "b",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "True",
                                                    "line": 4,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "True",
                                                        "line": 4,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "b",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "True",
                                                        "line": 4,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "True",
                                                        "line": 4,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "b",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "True",
                                                        "line": 4,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
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
                "1": "around the beginning of function 'test_function'"
            },
            "types": {
                "a": "*",
                "b": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def test_function():
    a = True
    b = False
    if not (not a and (not b)):
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function():\n    a = True\n    b = False\n    if not (not a and (not b)):\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "a",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "b",
                        "val1": {
                            "value": "False",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
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
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "a",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "b",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
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
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "b",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
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
                "1": "around the beginning of function 'test_function'"
            },
            "types": {
                "a": "*",
                "b": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def test_function():
    a = True
    b = False
    if not (not (a and True) and (not (b and True))):
        return True
    else:
        return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def test_function():\n    a = True\n    b = False\n    if not (not (a and True) and (not (b and True))):\n        return True\n    else:\n        return False"
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
        "test_function": {
            "name": "test_function",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "a",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "b",
                        "val1": {
                            "value": "False",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "value": "False",
                                "line": 3
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
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "And",
                                                            "args": [
                                                                {
                                                                    "name": "a",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "True",
                                                                    "line": 4,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 4,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Not",
                                                    "args": [
                                                        {
                                                            "name": "And",
                                                            "args": [
                                                                {
                                                                    "name": "b",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "True",
                                                                    "line": 4,
                                                                    "tokentype": "Constant"
                                                                }
                                                            ],
                                                            "line": 4,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 5,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "False",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
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
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "a",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "True",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 4,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "b",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "True",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 4,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "a",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "True",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 4,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Not",
                                                        "args": [
                                                            {
                                                                "name": "And",
                                                                "args": [
                                                                    {
                                                                        "name": "b",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "True",
                                                                        "line": 4,
                                                                        "tokentype": "Constant"
                                                                    }
                                                                ],
                                                                "line": 4,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "False",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
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
                "1": "around the beginning of function 'test_function'"
            },
            "types": {
                "a": "*",
                "b": "*"
            }
        }
    }
}
```

</details>

