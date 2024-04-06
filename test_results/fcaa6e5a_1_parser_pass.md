# Test Report

Time: 2024-04-06 15:51:14.935894

### Base Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

## Test Case 1

### Modified Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	i = 0
	while i < len(original_list):
		if original_list[i] % 2 == 0:
			filtered_list.append(original_list[i])
		i = i + 1
	return filtered_list
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\toriginal_list = [1, 2, 3, 4, 5]\n\tfiltered_list = []\n\ti = 0\n\twhile i < len(original_list):\n\t\tif original_list[i] % 2 == 0:\n\t\t\tfiltered_list.append(original_list[i])\n\t\ti = i + 1\n\treturn filtered_list"
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
        "main": {
            "name": "main",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "original_list",
                        "val1": {
                            "name": "ListInit",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "2",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "3",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "4",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "value": "5",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "original_list",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "3",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "4",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "5",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "original_list",
                            {
                                "name": "ListInit",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "2",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "3",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "4",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "5",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "filtered_list",
                        "val1": {
                            "name": "ListInit",
                            "args": [],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "filtered_list",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "filtered_list",
                            {
                                "name": "ListInit",
                                "args": [],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "i",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "original_list",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "original_list",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "original_list",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
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
                            "name": "filtered_list",
                            "primed": false,
                            "line": 9,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "filtered_list",
                                "primed": false,
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "filtered_list",
                                "primed": false,
                                "line": 9
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "filtered_list",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "original_list",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "2",
                                                    "line": 6,
                                                    "tokentype": "Constant"
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
                                {
                                    "name": "append",
                                    "args": [
                                        {
                                            "name": "filtered_list",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "original_list",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "filtered_list",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "filtered_list",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "original_list",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 6,
                                                        "tokentype": "Constant"
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
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "filtered_list",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "original_list",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "filtered_list",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "filtered_list",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "original_list",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "2",
                                                        "line": 6,
                                                        "tokentype": "Constant"
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
                                    {
                                        "name": "append",
                                        "args": [
                                            {
                                                "name": "filtered_list",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "original_list",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "filtered_list",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "i",
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
                            "i",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                            "i",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "i",
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
                "1": "around the beginning of function 'main'",
                "2": "the condition of the 'while' loop at line 5",
                "3": "*after* the 'while' loop starting at line 5",
                "4": "inside the body of the 'while' loop beginning at line 6"
            },
            "types": {
                "original_list": "*",
                "filtered_list": "*",
                "i": "*"
            }
        }
    }
}
```

</details>

