# Issue 11: Replacing For Range Loops with While Loops

## Description
This issue was caught by one of our metamorphic relations, which is `ForRangeToWhileLoopModifier`. In Python, there is a syntax of `for ... in range(...)`. It is possible to replace it with an equivalent `while` loop that produces the same equivalent program. With our modifier, we managed to show that 2 equivalent programs were deemed as unequivalent by the `errorlocalizer`, `feedback_error`, `feedback_fix` and `repair` endpoints even though they have the same semantics and return the same outputs.

### Base Program

```py
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

### Modified Program
```py
def func(x):
    x = x + 1
    j = 2
    while j < 5:
        x += 1
        j = j + 1
    return x
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"j\", \"val1\": {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"j\", {\"value\": \"2\", \"line\": 3}], \"valueList\": [\"j\", {\"value\": \"2\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"j\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"j\", {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"x\": \"*\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[[98], [97], [61], [40], [90], [19], [9], [79], [6], [65]]"
}
```

### Output

#### Error Localizer
```json
{
    "errorLocations": {
        "func": [
            [
                [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
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
                            "name": "x",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "x",
                            "primed": false,
                            "line": 2
                        }
                    ]
                ],
                [
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "x",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy1",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "j",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    }
                ]
            ]
        ]
    },
    "errorInputs": []
}
```

#### Feedback Error
```json
[
    {
        "lineNumber": 3,
        "hintStrings": [
            "Incorrect/Unnecessary expression assigned to variable: *j*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy2*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    },
    {
        "lineNumber": 4,
        "hintStrings": [
            "Wrong loop condition: (j < 5)"
        ]
    },
    {
        "lineNumber": 6,
        "hintStrings": [
            "Wrong expression for variable: *j*"
        ]
    },
    {
        "lineNumber": 4,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    }
]
```

#### Feedback Fix
```json
[
    {
        "lineNumber": 3,
        "oldExpr": "j = 2",
        "newExpr": "",
        "repairStrings": [
            "Delete j = 2;"
        ]
    },
    {
        "lineNumber": 1,
        "oldExpr": "",
        "newExpr": "dummy2 = range(2, 5);",
        "repairStrings": [
            "Add dummy2 = range(2, 5);;"
        ]
    },
    {
        "lineNumber": 1,
        "oldExpr": "",
        "newExpr": "dummy1 = 0",
        "repairStrings": [
            "Add dummy1 = 0;"
        ]
    },
    {
        "lineNumber": 4,
        "oldExpr": "(j < 5)",
        "newExpr": "(dummy1 < len(dummy2);)",
        "repairStrings": [
            "Error with loop condition",
            "Wrong loop condition. Change (j < 5) to (dummy1 < len(dummy2);)"
        ]
    },
    {
        "lineNumber": 6,
        "oldExpr": "j = (j + 1)",
        "newExpr": "j = dummy2[dummy1]",
        "repairStrings": [
            "Wrong expression. Change j = (j + 1); to j = dummy2[dummy1];"
        ]
    },
    {
        "lineNumber": 4,
        "oldExpr": "",
        "newExpr": "dummy1 = (dummy1 + 1)",
        "repairStrings": [
            "Add dummy1 = (dummy1 + 1);"
        ]
    }
]
```

#### Repair
```json
[
    {
        "totalCost": 14.0,
        "localRepairs": [
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
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
                            "name": "x",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "x",
                            "primed": false,
                            "line": 2
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "j",
                        "primed": false,
                        "line": 4
                    },
                    "val1": {
                        "tokentype": "Constant",
                        "value": "2",
                        "line": 3
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Constant",
                            "value": "2",
                            "line": 3
                        },
                        null
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Constant",
                            "value": "2",
                            "line": 3
                        },
                        null
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
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
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
                            "name": "x",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "x",
                            "primed": false,
                            "line": 2
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 10.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "dummy2",
                        "primed": false,
                        "line": 0
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "range",
                        "args": [
                            {
                                "tokentype": "Constant",
                                "value": "2",
                                "line": 3
                            },
                            {
                                "tokentype": "Constant",
                                "value": "5",
                                "line": 3
                            }
                        ],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Operation",
                            "name": "range",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 3
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 3
                                }
                            ],
                            "line": 0
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Operation",
                            "name": "range",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 3
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 3
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
                "funcName": "func"
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
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
                            "name": "x",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "x",
                            "primed": false,
                            "line": 2
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "j",
                            "primed": false,
                            "line": 4
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "dummy1",
                        "primed": false,
                        "line": 0
                    },
                    "val2": {
                        "tokentype": "Constant",
                        "value": "0",
                        "line": 3
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 3
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 3
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

## Related Test Reports
Refer to Test Report ID 406b0112.