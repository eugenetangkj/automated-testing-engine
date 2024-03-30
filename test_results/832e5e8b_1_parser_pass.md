# Test Report

Time: 2024-03-30 07:25:34.791533

### Base Program

```py
from itertools import permutations as perm

def reorderedPowerOf2(n):
    for p in set(perm(str(n))):
        if p[0] != '0' and (bin(int(''.join(p))).count('1') == 1):
            return True
    return False
```

## Test Case 1

### Modified Program

```py
from itertools import permutations as perm

def reorderedPowerOf2(n):
    for p in set(perm(str(n))):
        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:
            return True
    return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from itertools import permutations as perm\n\ndef reorderedPowerOf2(n):\n    for p in set(perm(str(n))):\n        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:\n            return True\n    return False"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "from itertools import permutations as perm"
    ],
    "fncs": {
        "reorderedPowerOf2": {
            "name": "reorderedPowerOf2",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "n",
                    "val1": "*",
                    "valueArray": [
                        "n",
                        "*"
                    ],
                    "valueList": [
                        "n",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "set",
                            "args": [
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "perm",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "str",
                                            "args": [
                                                {
                                                    "name": "n",
                                                    "primed": false,
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "n",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "value": "False",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "p",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "\"0\"",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "count",
                                                    "args": [
                                                        {
                                                            "name": "bin",
                                                            "args": [
                                                                {
                                                                    "name": "int",
                                                                    "args": [
                                                                        {
                                                                            "name": "FuncCall",
                                                                            "args": [
                                                                                {
                                                                                    "value": "join",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "value": "\"\"",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "name": "p",
                                                                                    "primed": true,
                                                                                    "line": 5,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 5,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 5,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 5,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "\"1\"",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
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
                "1": "around the beginning of function 'reorderedPowerOf2'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "p": "*",
                "ind#0": "int",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
from itertools import permutations as perm

def reorderedPowerOf2(var_0):
    for p in set(perm(str(var_0))):
        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:
            return True
    return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from itertools import permutations as perm\n\ndef reorderedPowerOf2(var_0):\n    for p in set(perm(str(var_0))):\n        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:\n            return True\n    return False"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "from itertools import permutations as perm"
    ],
    "fncs": {
        "reorderedPowerOf2": {
            "name": "reorderedPowerOf2",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "set",
                            "args": [
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "perm",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "str",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "value": "False",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "p",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "\"0\"",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "count",
                                                    "args": [
                                                        {
                                                            "name": "bin",
                                                            "args": [
                                                                {
                                                                    "name": "int",
                                                                    "args": [
                                                                        {
                                                                            "name": "FuncCall",
                                                                            "args": [
                                                                                {
                                                                                    "value": "join",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "value": "\"\"",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "name": "p",
                                                                                    "primed": true,
                                                                                    "line": 5,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 5,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 5,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 5,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "\"1\"",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
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
                "1": "around the beginning of function 'reorderedPowerOf2'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "p": "*",
                "ind#0": "int",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
from itertools import permutations as perm

def reorderedPowerOf2(var_1):
    for p in set(perm(str(var_1))):
        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:
            return True
    return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from itertools import permutations as perm\n\ndef reorderedPowerOf2(var_1):\n    for p in set(perm(str(var_1))):\n        if p[0] != '0' and bin(int(''.join(p))).count('1') == 1:\n            return True\n    return False"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [
        "from itertools import permutations as perm"
    ],
    "fncs": {
        "reorderedPowerOf2": {
            "name": "reorderedPowerOf2",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "set",
                            "args": [
                                {
                                    "name": "FuncCall",
                                    "args": [
                                        {
                                            "value": "perm",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "str",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "set",
                                "args": [
                                    {
                                        "name": "FuncCall",
                                        "args": [
                                            {
                                                "value": "perm",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "str",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
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
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "value": "False",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "False",
                                "line": 7
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "p",
                                                            "primed": true,
                                                            "line": 5,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "\"0\"",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "count",
                                                    "args": [
                                                        {
                                                            "name": "bin",
                                                            "args": [
                                                                {
                                                                    "name": "int",
                                                                    "args": [
                                                                        {
                                                                            "name": "FuncCall",
                                                                            "args": [
                                                                                {
                                                                                    "value": "join",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "value": "\"\"",
                                                                                    "line": 5,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "name": "p",
                                                                                    "primed": true,
                                                                                    "line": 5,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 5,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 5,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 5,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "\"1\"",
                                                            "line": 5,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 5,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "True",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "p",
                                                                "primed": true,
                                                                "line": 5,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "\"0\"",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "count",
                                                        "args": [
                                                            {
                                                                "name": "bin",
                                                                "args": [
                                                                    {
                                                                        "name": "int",
                                                                        "args": [
                                                                            {
                                                                                "name": "FuncCall",
                                                                                "args": [
                                                                                    {
                                                                                        "value": "join",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "\"\"",
                                                                                        "line": 5,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "name": "p",
                                                                                        "primed": true,
                                                                                        "line": 5,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 5,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 5,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 5,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "\"1\"",
                                                                "line": 5,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 5,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "True",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "$ret",
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
                "1": "around the beginning of function 'reorderedPowerOf2'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5"
            },
            "types": {
                "p": "*",
                "ind#0": "int",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

