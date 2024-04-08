# Test Report

Time: 2024-04-08 07:48:45.606032

### Base Program

```py
def main():
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

## Test Case 1

### Modified Program

```py
def main():
	curr_string = 'Hello World'
	try:
		index = curr_string.index('Hello')
		return True
	except ValueError:
		return False
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def main():\n\tcurr_string = 'Hello World'\n\ttry:\n\t\tindex = curr_string.index('Hello')\n\t\treturn True\n\texcept ValueError:\n\t\treturn False"
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
                        "val0": "curr_string",
                        "val1": {
                            "value": "\"Hello World\"",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "curr_string",
                            {
                                "value": "\"Hello World\"",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "curr_string",
                            {
                                "value": "\"Hello World\"",
                                "line": 2
                            }
                        ]
                    },
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'main'"
            },
            "types": {
                "curr_string": "*"
            }
        }
    }
}
```

</details>

