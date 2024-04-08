# Test Report

Time: 2024-04-08 08:52:17.601911

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
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def func():\n    return 100"
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
        "func": {
            "name": "func",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "value": "100",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "100",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "100",
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
                "1": "around the beginning of function 'func'"
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
def func():
    try:
        return 100
    except:
        return 1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def func():\n    try:\n        return 100\n    except:\n        return 1"
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
        "func": {
            "name": "func",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "value": "1",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'func'"
            },
            "types": {}
        }
    }
}
```

</details>

