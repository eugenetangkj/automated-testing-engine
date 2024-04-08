# Test Report

Time: 2024-04-08 07:53:32.115429

### Base Program

```py
def main():
	return 1
```

## Test Case 1

### Modified Program

```py
def main():
	try:
		return 1
	except:
		return 0
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\ttry:\n\t\treturn 1\n\texcept:\n\t\treturn 0"
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
                        "val0": "$ret",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "value": "0",
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
                "1": "around the beginning of function 'main'"
            },
            "types": {}
        }
    }
}
```

</details>

