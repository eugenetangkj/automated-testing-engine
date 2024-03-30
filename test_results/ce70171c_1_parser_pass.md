# Test Report

Time: 2024-03-30 08:21:49.007598

### Base Program

```py
def min_health(damage, armor):
    health = 0
    for dmg in reversed(damage):
        health += dmg
        if health > armor:
            health -= armor
            armor = 0
    return health + 1
```

## Test Case 1

### Modified Program

```py
def min_health(damage, armor):
    health = 0
    for dmg in reversed(damage):
        health += dmg
        if health > armor:
            health -= armor
            armor = 0
    return health + 1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_health(damage, armor):\n    health = 0\n    for dmg in reversed(damage):\n        health += dmg\n        if health > armor:\n            health -= armor\n            armor = 0\n    return health + 1"
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
        "min_health": {
            "name": "min_health",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "damage",
                    "val1": "*",
                    "valueArray": [
                        "damage",
                        "*"
                    ],
                    "valueList": [
                        "damage",
                        "*"
                    ]
                },
                {
                    "val0": "armor",
                    "val1": "*",
                    "valueArray": [
                        "armor",
                        "*"
                    ],
                    "valueList": [
                        "armor",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "health",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "reversed",
                            "args": [
                                {
                                    "name": "damage",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "damage",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "damage",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "health",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "dmg",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "health",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "health",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "dmg",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "armor",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "armor",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "armor",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "armor",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "armor",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "armor",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_health'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "armor": "*",
                "ind#0": "int",
                "health": "*",
                "iter#0": "int",
                "dmg": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def min_health(var_0, var_1):
    health = 0
    for dmg in reversed(var_0):
        health += dmg
        if health > var_1:
            health -= var_1
            var_1 = 0
    return health + 1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_health(var_0, var_1):\n    health = 0\n    for dmg in reversed(var_0):\n        health += dmg\n        if health > var_1:\n            health -= var_1\n            var_1 = 0\n    return health + 1"
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
        "min_health": {
            "name": "min_health",
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
                        "val0": "health",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "reversed",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "health",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "dmg",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "health",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "health",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "dmg",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "var_1",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_1",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_health'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "var_1": "*",
                "ind#0": "int",
                "health": "*",
                "iter#0": "int",
                "dmg": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def min_health(damage, armor):
    health = 0
    for dmg in reversed(damage):
        health += dmg
        if health > armor:
            health -= armor
            armor = 0
    return 1 + health
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_health(damage, armor):\n    health = 0\n    for dmg in reversed(damage):\n        health += dmg\n        if health > armor:\n            health -= armor\n            armor = 0\n    return 1 + health"
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
        "min_health": {
            "name": "min_health",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "damage",
                    "val1": "*",
                    "valueArray": [
                        "damage",
                        "*"
                    ],
                    "valueList": [
                        "damage",
                        "*"
                    ]
                },
                {
                    "val0": "armor",
                    "val1": "*",
                    "valueArray": [
                        "armor",
                        "*"
                    ],
                    "valueList": [
                        "armor",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "health",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "reversed",
                            "args": [
                                {
                                    "name": "damage",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "damage",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "damage",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "health",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "dmg",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "health",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "health",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "dmg",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "armor",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "armor",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "armor",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "armor",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "armor",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "armor",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "armor",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "armor",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_health'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "armor": "*",
                "ind#0": "int",
                "health": "*",
                "iter#0": "int",
                "dmg": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def min_health(var_2, var_3):
    health = 0
    for dmg in reversed(var_2):
        health += dmg
        if health > var_3:
            health -= var_3
            var_3 = 0
    return 1 + health
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_health(var_2, var_3):\n    health = 0\n    for dmg in reversed(var_2):\n        health += dmg\n        if health > var_3:\n            health -= var_3\n            var_3 = 0\n    return 1 + health"
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
        "min_health": {
            "name": "min_health",
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
                        "val0": "health",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "reversed",
                            "args": [
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "reversed",
                                "args": [
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "health",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "health",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "dmg",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dmg",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "health",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "health",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "dmg",
                                            "primed": true,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "health",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "health",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "dmg",
                                                "primed": true,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "var_3",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "health",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "dmg",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "var_3",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 7,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_3",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_3",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "health",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "dmg",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "var_3",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_health'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ind#0": "int",
                "var_3": "*",
                "health": "*",
                "iter#0": "int",
                "dmg": "*"
            }
        }
    }
}
```

</details>

