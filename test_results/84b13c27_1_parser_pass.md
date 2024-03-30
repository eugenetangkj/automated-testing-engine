# Test Report

Time: 2024-03-30 07:41:35.896805

### Base Program

```py
def numberOfNiceDivisors(primeFactors):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= primeFactors:
        if primeFactors % p == 0:
            count = 0
            while primeFactors % p == 0:
                primeFactors //= p
                count += 1
            result = (result * (count * 2 + 1)) % MOD
        p += 1
    return result
```

## Test Case 1

### Modified Program

```py
def numberOfNiceDivisors(primeFactors):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= primeFactors:
        if primeFactors % p == 0:
            count = 0
            while primeFactors % p == 0:
                primeFactors //= p
                count += 1
            result = result * (count * 2 + 1) % MOD
        p += 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def numberOfNiceDivisors(primeFactors):\n    MOD = 1000000007\n    result = 1\n    p = 2\n    while p <= primeFactors:\n        if primeFactors % p == 0:\n            count = 0\n            while primeFactors % p == 0:\n                primeFactors //= p\n                count += 1\n            result = result * (count * 2 + 1) % MOD\n        p += 1\n    return result"
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
        "numberOfNiceDivisors": {
            "name": "numberOfNiceDivisors",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "primeFactors",
                    "val1": "*",
                    "valueArray": [
                        "primeFactors",
                        "*"
                    ],
                    "valueList": [
                        "primeFactors",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "MOD",
                        "val1": {
                            "value": "1000000007",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "2",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "LtE",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "primeFactors",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "primeFactors",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "primeFactors",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "result",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "count",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "MOD",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "primeFactors",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "primeFactors",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "primeFactors",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "primeFactors",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                    "true": 5
                },
                "5": {
                    "false": 10,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'numberOfNiceDivisors'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "7": "the condition of the 'while' loop at line 8",
                "8": "*after* the 'while' loop starting at line 8",
                "9": "inside the body of the 'while' loop beginning at line 9",
                "10": "after the if-statement beginning at line 6"
            },
            "types": {
                "result": "*",
                "p": "*",
                "MOD": "*",
                "count": "*",
                "primeFactors": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def numberOfNiceDivisors(var_0):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= var_0:
        if var_0 % p == 0:
            count = 0
            while var_0 % p == 0:
                var_0 //= p
                count += 1
            result = result * (count * 2 + 1) % MOD
        p += 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def numberOfNiceDivisors(var_0):\n    MOD = 1000000007\n    result = 1\n    p = 2\n    while p <= var_0:\n        if var_0 % p == 0:\n            count = 0\n            while var_0 % p == 0:\n                var_0 //= p\n                count += 1\n            result = result * (count * 2 + 1) % MOD\n        p += 1\n    return result"
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
        "numberOfNiceDivisors": {
            "name": "numberOfNiceDivisors",
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
                        "val0": "MOD",
                        "val1": {
                            "value": "1000000007",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "2",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "LtE",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "result",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "count",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "MOD",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "var_0",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_0",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "var_0",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                    "true": 5
                },
                "5": {
                    "false": 10,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'numberOfNiceDivisors'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "7": "the condition of the 'while' loop at line 8",
                "8": "*after* the 'while' loop starting at line 8",
                "9": "inside the body of the 'while' loop beginning at line 9",
                "10": "after the if-statement beginning at line 6"
            },
            "types": {
                "result": "*",
                "p": "*",
                "MOD": "*",
                "var_0": "*",
                "count": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def numberOfNiceDivisors(primeFactors):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= primeFactors:
        if primeFactors % p == 0:
            count = 0
            while primeFactors % p == 0:
                primeFactors //= p
                count += 1
            result = (1 + 2 * count) * result % MOD
        p += 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def numberOfNiceDivisors(primeFactors):\n    MOD = 1000000007\n    result = 1\n    p = 2\n    while p <= primeFactors:\n        if primeFactors % p == 0:\n            count = 0\n            while primeFactors % p == 0:\n                primeFactors //= p\n                count += 1\n            result = (1 + 2 * count) * result % MOD\n        p += 1\n    return result"
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
        "numberOfNiceDivisors": {
            "name": "numberOfNiceDivisors",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "primeFactors",
                    "val1": "*",
                    "valueArray": [
                        "primeFactors",
                        "*"
                    ],
                    "valueList": [
                        "primeFactors",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "MOD",
                        "val1": {
                            "value": "1000000007",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "2",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "LtE",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "primeFactors",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "primeFactors",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "primeFactors",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "primeFactors",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "value": "2",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "count",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "result",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "MOD",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "primeFactors",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "primeFactors",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "primeFactors",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "primeFactors",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "primeFactors",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                    "true": 5
                },
                "5": {
                    "false": 10,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'numberOfNiceDivisors'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "7": "the condition of the 'while' loop at line 8",
                "8": "*after* the 'while' loop starting at line 8",
                "9": "inside the body of the 'while' loop beginning at line 9",
                "10": "after the if-statement beginning at line 6"
            },
            "types": {
                "result": "*",
                "p": "*",
                "MOD": "*",
                "count": "*",
                "primeFactors": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def numberOfNiceDivisors(var_1):
    MOD = 1000000007
    result = 1
    p = 2
    while p <= var_1:
        if var_1 % p == 0:
            count = 0
            while var_1 % p == 0:
                var_1 //= p
                count += 1
            result = (1 + 2 * count) * result % MOD
        p += 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def numberOfNiceDivisors(var_1):\n    MOD = 1000000007\n    result = 1\n    p = 2\n    while p <= var_1:\n        if var_1 % p == 0:\n            count = 0\n            while var_1 % p == 0:\n                var_1 //= p\n                count += 1\n            result = (1 + 2 * count) * result % MOD\n        p += 1\n    return result"
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
        "numberOfNiceDivisors": {
            "name": "numberOfNiceDivisors",
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
                        "val0": "MOD",
                        "val1": {
                            "value": "1000000007",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "MOD",
                            {
                                "value": "1000000007",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "result",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "2",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "2",
                                "line": 4
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "LtE",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "LtE",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "result",
                            "primed": false,
                            "line": 13,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 13
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "value": "2",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "count",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "result",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "MOD",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "value": "2",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "count",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "result",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "MOD",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "var_1",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_1",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    }
                ],
                "10": [
                    {
                        "val0": "p",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "p",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "p",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                    "true": 5
                },
                "5": {
                    "false": 10,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'numberOfNiceDivisors'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6",
                "5": "the condition of the if-statement at line 6",
                "6": "inside the if-branch starting at line 7",
                "7": "the condition of the 'while' loop at line 8",
                "8": "*after* the 'while' loop starting at line 8",
                "9": "inside the body of the 'while' loop beginning at line 9",
                "10": "after the if-statement beginning at line 6"
            },
            "types": {
                "result": "*",
                "p": "*",
                "MOD": "*",
                "var_1": "*",
                "count": "*"
            }
        }
    }
}
```

</details>

