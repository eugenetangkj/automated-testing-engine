# Test Report

Time: 2024-04-06 12:59:14.372107

### Base Program

```py
def main():
	x = 2
	return x
```

## Test Case 1

### Modified Program

```py
def main():
	x = 2
		return x
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\tx = 2\n\t\treturn x"
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
                        "val0": "x",
                        "val1": {
                            "value": "2",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "x",
                            {
                                "value": "2",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "value": "2",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "x",
                            "primed": true,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "x",
                                "primed": true,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "x",
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
                "1": "around the beginning of function 'main'"
            },
            "types": {
                "x": "*"
            }
        }
    }
}
```

</details>

