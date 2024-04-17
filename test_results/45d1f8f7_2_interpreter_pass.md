# Test Report

Time: 2024-04-16 12:24 AM

### Base Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

## Test Case 1

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[39, 1]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 39,
                "exponent": 1
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 39,
                "exponent": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 39,
                "$cond'": true,
                "exponent'": 0,
                "base": 39,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 39,
                "result'": 39,
                "$cond'": false,
                "exponent'": 0,
                "base": 39,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 39,
                "result'": 39,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 39,
                "base": 39,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 2

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[62, 75]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 62,
                "exponent": 75
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 62,
                "exponent": 75,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 62,
                "$cond'": true,
                "exponent'": 74,
                "base": 62,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 62,
                "result'": 62,
                "$cond'": true,
                "exponent'": 74,
                "base": 62,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 62,
                "result'": 3844,
                "$cond'": true,
                "exponent'": 73,
                "base": 62,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 3844,
                "result'": 3844,
                "$cond'": true,
                "exponent'": 73,
                "base": 62,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 3844,
                "result'": 238328,
                "$cond'": true,
                "exponent'": 72,
                "base": 62,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 238328,
                "result'": 238328,
                "$cond'": true,
                "exponent'": 72,
                "base": 62,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 238328,
                "result'": 14776336,
                "$cond'": true,
                "exponent'": 71,
                "base": 62,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 14776336,
                "result'": 14776336,
                "$cond'": true,
                "exponent'": 71,
                "base": 62,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 14776336,
                "result'": 916132832,
                "$cond'": true,
                "exponent'": 70,
                "base": 62,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 916132832,
                "result'": 916132832,
                "$cond'": true,
                "exponent'": 70,
                "base": 62,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 916132832,
                "result'": 965660736,
                "$cond'": true,
                "exponent'": 69,
                "base": 62,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 965660736,
                "result'": 965660736,
                "$cond'": true,
                "exponent'": 69,
                "base": 62,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 965660736,
                "result'": -258576512,
                "$cond'": true,
                "exponent'": 68,
                "base": 62,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -258576512,
                "result'": -258576512,
                "$cond'": true,
                "exponent'": 68,
                "base": 62,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -258576512,
                "result'": 1148125440,
                "$cond'": true,
                "exponent'": 67,
                "base": 62,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1148125440,
                "result'": 1148125440,
                "$cond'": true,
                "exponent'": 67,
                "base": 62,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1148125440,
                "result'": -1830666752,
                "$cond'": true,
                "exponent'": 66,
                "base": 62,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1830666752,
                "result'": -1830666752,
                "$cond'": true,
                "exponent'": 66,
                "base": 62,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1830666752,
                "result'": -1832188928,
                "$cond'": true,
                "exponent'": 65,
                "base": 62,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1832188928,
                "result'": -1832188928,
                "$cond'": true,
                "exponent'": 65,
                "base": 62,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1832188928,
                "result'": -1926563840,
                "$cond'": true,
                "exponent'": 64,
                "base": 62,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1926563840,
                "result'": -1926563840,
                "$cond'": true,
                "exponent'": 64,
                "base": 62,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1926563840,
                "result'": 812126208,
                "$cond'": true,
                "exponent'": 63,
                "base": 62,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 812126208,
                "result'": 812126208,
                "$cond'": true,
                "exponent'": 63,
                "base": 62,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 812126208,
                "result'": -1187782656,
                "$cond'": true,
                "exponent'": 62,
                "base": 62,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1187782656,
                "result'": -1187782656,
                "$cond'": true,
                "exponent'": 62,
                "base": 62,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1187782656,
                "result'": -628080640,
                "$cond'": true,
                "exponent'": 61,
                "base": 62,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -628080640,
                "result'": -628080640,
                "$cond'": true,
                "exponent'": 61,
                "base": 62,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -628080640,
                "result'": -286294016,
                "$cond'": true,
                "exponent'": 60,
                "base": 62,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -286294016,
                "result'": -286294016,
                "$cond'": true,
                "exponent'": 60,
                "base": 62,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -286294016,
                "result'": -570359808,
                "$cond'": true,
                "exponent'": 59,
                "base": 62,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -570359808,
                "result'": -570359808,
                "$cond'": true,
                "exponent'": 59,
                "base": 62,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -570359808,
                "result'": -1002569728,
                "$cond'": true,
                "exponent'": 58,
                "base": 62,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1002569728,
                "result'": -1002569728,
                "$cond'": true,
                "exponent'": 58,
                "base": 62,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1002569728,
                "result'": -2029780992,
                "$cond'": true,
                "exponent'": 57,
                "base": 62,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2029780992,
                "result'": -2029780992,
                "$cond'": true,
                "exponent'": 57,
                "base": 62,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2029780992,
                "result'": -1292369920,
                "$cond'": true,
                "exponent'": 56,
                "base": 62,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1292369920,
                "result'": -1292369920,
                "$cond'": true,
                "exponent'": 56,
                "base": 62,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1292369920,
                "result'": 1477443584,
                "$cond'": true,
                "exponent'": 55,
                "base": 62,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1477443584,
                "result'": 1477443584,
                "$cond'": true,
                "exponent'": 55,
                "base": 62,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1477443584,
                "result'": 1407188992,
                "$cond'": true,
                "exponent'": 54,
                "base": 62,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1407188992,
                "result'": 1407188992,
                "$cond'": true,
                "exponent'": 54,
                "base": 62,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1407188992,
                "result'": 1346371584,
                "$cond'": true,
                "exponent'": 53,
                "base": 62,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1346371584,
                "result'": 1346371584,
                "$cond'": true,
                "exponent'": 53,
                "base": 62,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1346371584,
                "result'": 1870659584,
                "$cond'": true,
                "exponent'": 52,
                "base": 62,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1870659584,
                "result'": 1870659584,
                "$cond'": true,
                "exponent'": 52,
                "base": 62,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1870659584,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 51,
                "base": 62,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 16777216,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 51,
                "base": 62,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 16777216,
                "result'": 1040187392,
                "$cond'": true,
                "exponent'": 50,
                "base": 62,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1040187392,
                "result'": 1040187392,
                "$cond'": true,
                "exponent'": 50,
                "base": 62,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1040187392,
                "result'": 67108864,
                "$cond'": true,
                "exponent'": 49,
                "base": 62,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 67108864,
                "result'": 67108864,
                "$cond'": true,
                "exponent'": 49,
                "base": 62,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 67108864,
                "result'": -134217728,
                "$cond'": true,
                "exponent'": 48,
                "base": 62,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -134217728,
                "result'": -134217728,
                "$cond'": true,
                "exponent'": 48,
                "base": 62,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -134217728,
                "result'": 268435456,
                "$cond'": true,
                "exponent'": 47,
                "base": 62,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 268435456,
                "result'": 268435456,
                "$cond'": true,
                "exponent'": 47,
                "base": 62,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 268435456,
                "result'": -536870912,
                "$cond'": true,
                "exponent'": 46,
                "base": 62,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -536870912,
                "result'": -536870912,
                "$cond'": true,
                "exponent'": 46,
                "base": 62,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -536870912,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 45,
                "base": 62,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1073741824,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 45,
                "base": 62,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1073741824,
                "result'": -2147483648,
                "$cond'": true,
                "exponent'": 44,
                "base": 62,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2147483648,
                "result'": -2147483648,
                "$cond'": true,
                "exponent'": 44,
                "base": 62,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2147483648,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 62,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 62,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 62,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 62,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 62,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 62,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 62,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 62,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 62,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 62,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 62,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 62,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 62,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 62,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 62,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 62,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 62,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 62,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 62,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 62,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 62,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 62,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 62,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 62,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 62,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 62,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 62,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 62,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 62,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 62,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 62,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 62,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 62,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 62,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 62,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 62,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 62,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 62,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 62,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 62,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 62,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 62,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 62,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 62,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 62,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 62,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 62,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 62,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 62,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 62,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 62,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 62,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 62,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 62,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 62,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 62,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 62,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 62,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 62,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 62,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 62,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 62,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 62,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 62,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 62,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 62,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 62,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 62,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 62,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 62,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 62,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 62,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 62,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 62,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 62,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 62,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 62,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 62,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 62,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 62,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 62,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 62,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 62,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 62,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 62,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 62,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 0,
                "base": 62,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "base": 62,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 0,
                "base": 62,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 3

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[75, 84]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 75,
                "exponent": 84
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 75,
                "exponent": 84,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 75,
                "$cond'": true,
                "exponent'": 83,
                "base": 75,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 75,
                "result'": 75,
                "$cond'": true,
                "exponent'": 83,
                "base": 75,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 75,
                "result'": 5625,
                "$cond'": true,
                "exponent'": 82,
                "base": 75,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 5625,
                "result'": 5625,
                "$cond'": true,
                "exponent'": 82,
                "base": 75,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 5625,
                "result'": 421875,
                "$cond'": true,
                "exponent'": 81,
                "base": 75,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 421875,
                "result'": 421875,
                "$cond'": true,
                "exponent'": 81,
                "base": 75,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 421875,
                "result'": 31640625,
                "$cond'": true,
                "exponent'": 80,
                "base": 75,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 31640625,
                "result'": 31640625,
                "$cond'": true,
                "exponent'": 80,
                "base": 75,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 31640625,
                "result'": -1921920421,
                "$cond'": true,
                "exponent'": 79,
                "base": 75,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1921920421,
                "result'": -1921920421,
                "$cond'": true,
                "exponent'": 79,
                "base": 75,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1921920421,
                "result'": 1884856489,
                "$cond'": true,
                "exponent'": 78,
                "base": 75,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1884856489,
                "result'": 1884856489,
                "$cond'": true,
                "exponent'": 78,
                "base": 75,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1884856489,
                "result'": -369684093,
                "$cond'": true,
                "exponent'": 77,
                "base": 75,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -369684093,
                "result'": -369684093,
                "$cond'": true,
                "exponent'": 77,
                "base": 75,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -369684093,
                "result'": -1956503199,
                "$cond'": true,
                "exponent'": 76,
                "base": 75,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1956503199,
                "result'": -1956503199,
                "$cond'": true,
                "exponent'": 76,
                "base": 75,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1956503199,
                "result'": -708851861,
                "$cond'": true,
                "exponent'": 75,
                "base": 75,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -708851861,
                "result'": -708851861,
                "$cond'": true,
                "exponent'": 75,
                "base": 75,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -708851861,
                "result'": -1624282023,
                "$cond'": true,
                "exponent'": 74,
                "base": 75,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1624282023,
                "result'": -1624282023,
                "$cond'": true,
                "exponent'": 74,
                "base": 75,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1624282023,
                "result'": -1562067437,
                "$cond'": true,
                "exponent'": 73,
                "base": 75,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1562067437,
                "result'": -1562067437,
                "$cond'": true,
                "exponent'": 73,
                "base": 75,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1562067437,
                "result'": -1190940783,
                "$cond'": true,
                "exponent'": 72,
                "base": 75,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1190940783,
                "result'": -1190940783,
                "$cond'": true,
                "exponent'": 72,
                "base": 75,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1190940783,
                "result'": 873754491,
                "$cond'": true,
                "exponent'": 71,
                "base": 75,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 873754491,
                "result'": 873754491,
                "$cond'": true,
                "exponent'": 71,
                "base": 75,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 873754491,
                "result'": 1107077385,
                "$cond'": true,
                "exponent'": 70,
                "base": 75,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1107077385,
                "result'": 1107077385,
                "$cond'": true,
                "exponent'": 70,
                "base": 75,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1107077385,
                "result'": 1426425251,
                "$cond'": true,
                "exponent'": 69,
                "base": 75,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1426425251,
                "result'": 1426425251,
                "$cond'": true,
                "exponent'": 69,
                "base": 75,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1426425251,
                "result'": -392288575,
                "$cond'": true,
                "exponent'": 68,
                "base": 75,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -392288575,
                "result'": -392288575,
                "$cond'": true,
                "exponent'": 68,
                "base": 75,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -392288575,
                "result'": 643127947,
                "$cond'": true,
                "exponent'": 67,
                "base": 75,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 643127947,
                "result'": 643127947,
                "$cond'": true,
                "exponent'": 67,
                "base": 75,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 643127947,
                "result'": 989955769,
                "$cond'": true,
                "exponent'": 66,
                "base": 75,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 989955769,
                "result'": 989955769,
                "$cond'": true,
                "exponent'": 66,
                "base": 75,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 989955769,
                "result'": 1232238643,
                "$cond'": true,
                "exponent'": 65,
                "base": 75,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1232238643,
                "result'": 1232238643,
                "$cond'": true,
                "exponent'": 65,
                "base": 75,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1232238643,
                "result'": -2071382287,
                "$cond'": true,
                "exponent'": 64,
                "base": 75,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2071382287,
                "result'": -2071382287,
                "$cond'": true,
                "exponent'": 64,
                "base": 75,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2071382287,
                "result'": -734848869,
                "$cond'": true,
                "exponent'": 63,
                "base": 75,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -734848869,
                "result'": -734848869,
                "$cond'": true,
                "exponent'": 63,
                "base": 75,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -734848869,
                "result'": 720909673,
                "$cond'": true,
                "exponent'": 62,
                "base": 75,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 720909673,
                "result'": 720909673,
                "$cond'": true,
                "exponent'": 62,
                "base": 75,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 720909673,
                "result'": -1766349373,
                "$cond'": true,
                "exponent'": 61,
                "base": 75,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1766349373,
                "result'": -1766349373,
                "$cond'": true,
                "exponent'": 61,
                "base": 75,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1766349373,
                "result'": 667783201,
                "$cond'": true,
                "exponent'": 60,
                "base": 75,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 667783201,
                "result'": 667783201,
                "$cond'": true,
                "exponent'": 60,
                "base": 75,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 667783201,
                "result'": -1455867477,
                "$cond'": true,
                "exponent'": 59,
                "base": 75,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1455867477,
                "result'": -1455867477,
                "$cond'": true,
                "exponent'": 59,
                "base": 75,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1455867477,
                "result'": -1815878375,
                "$cond'": true,
                "exponent'": 58,
                "base": 75,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1815878375,
                "result'": -1815878375,
                "$cond'": true,
                "exponent'": 58,
                "base": 75,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1815878375,
                "result'": 1248075347,
                "$cond'": true,
                "exponent'": 57,
                "base": 75,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1248075347,
                "result'": 1248075347,
                "$cond'": true,
                "exponent'": 57,
                "base": 75,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1248075347,
                "result'": -883629487,
                "$cond'": true,
                "exponent'": 56,
                "base": 75,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -883629487,
                "result'": -883629487,
                "$cond'": true,
                "exponent'": 56,
                "base": 75,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -883629487,
                "result'": -1847702085,
                "$cond'": true,
                "exponent'": 55,
                "base": 75,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1847702085,
                "result'": -1847702085,
                "$cond'": true,
                "exponent'": 55,
                "base": 75,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1847702085,
                "result'": -1138702903,
                "$cond'": true,
                "exponent'": 54,
                "base": 75,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1138702903,
                "result'": -1138702903,
                "$cond'": true,
                "exponent'": 54,
                "base": 75,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1138702903,
                "result'": 496628195,
                "$cond'": true,
                "exponent'": 53,
                "base": 75,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 496628195,
                "result'": 496628195,
                "$cond'": true,
                "exponent'": 53,
                "base": 75,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 496628195,
                "result'": -1407591039,
                "$cond'": true,
                "exponent'": 52,
                "base": 75,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1407591039,
                "result'": -1407591039,
                "$cond'": true,
                "exponent'": 52,
                "base": 75,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1407591039,
                "result'": 1804854475,
                "$cond'": true,
                "exponent'": 51,
                "base": 75,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1804854475,
                "result'": 1804854475,
                "$cond'": true,
                "exponent'": 51,
                "base": 75,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1804854475,
                "result'": -2074867847,
                "$cond'": true,
                "exponent'": 50,
                "base": 75,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2074867847,
                "result'": -2074867847,
                "$cond'": true,
                "exponent'": 50,
                "base": 75,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2074867847,
                "result'": -996265869,
                "$cond'": true,
                "exponent'": 49,
                "base": 75,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -996265869,
                "result'": -996265869,
                "$cond'": true,
                "exponent'": 49,
                "base": 75,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -996265869,
                "result'": -1705496143,
                "$cond'": true,
                "exponent'": 48,
                "base": 75,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1705496143,
                "result'": -1705496143,
                "$cond'": true,
                "exponent'": 48,
                "base": 75,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1705496143,
                "result'": 936808155,
                "$cond'": true,
                "exponent'": 47,
                "base": 75,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 936808155,
                "result'": 936808155,
                "$cond'": true,
                "exponent'": 47,
                "base": 75,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 936808155,
                "result'": 1541134889,
                "$cond'": true,
                "exponent'": 46,
                "base": 75,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1541134889,
                "result'": 1541134889,
                "$cond'": true,
                "exponent'": 46,
                "base": 75,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1541134889,
                "result'": -379000317,
                "$cond'": true,
                "exponent'": 45,
                "base": 75,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -379000317,
                "result'": -379000317,
                "$cond'": true,
                "exponent'": 45,
                "base": 75,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -379000317,
                "result'": 1639747297,
                "$cond'": true,
                "exponent'": 44,
                "base": 75,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1639747297,
                "result'": 1639747297,
                "$cond'": true,
                "exponent'": 44,
                "base": 75,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1639747297,
                "result'": -1573004309,
                "$cond'": true,
                "exponent'": 43,
                "base": 75,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1573004309,
                "result'": -1573004309,
                "$cond'": true,
                "exponent'": 43,
                "base": 75,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1573004309,
                "result'": -2011206183,
                "$cond'": true,
                "exponent'": 42,
                "base": 75,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2011206183,
                "result'": -2011206183,
                "$cond'": true,
                "exponent'": 42,
                "base": 75,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2011206183,
                "result'": -516608365,
                "$cond'": true,
                "exponent'": 41,
                "base": 75,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -516608365,
                "result'": -516608365,
                "$cond'": true,
                "exponent'": 41,
                "base": 75,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -516608365,
                "result'": -90921711,
                "$cond'": true,
                "exponent'": 40,
                "base": 75,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -90921711,
                "result'": -90921711,
                "$cond'": true,
                "exponent'": 40,
                "base": 75,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -90921711,
                "result'": 1770806267,
                "$cond'": true,
                "exponent'": 39,
                "base": 75,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1770806267,
                "result'": 1770806267,
                "$cond'": true,
                "exponent'": 39,
                "base": 75,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1770806267,
                "result'": -333516151,
                "$cond'": true,
                "exponent'": 38,
                "base": 75,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -333516151,
                "result'": -333516151,
                "$cond'": true,
                "exponent'": 38,
                "base": 75,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -333516151,
                "result'": 756092451,
                "$cond'": true,
                "exponent'": 37,
                "base": 75,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 756092451,
                "result'": 756092451,
                "$cond'": true,
                "exponent'": 37,
                "base": 75,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 756092451,
                "result'": 872358977,
                "$cond'": true,
                "exponent'": 36,
                "base": 75,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 872358977,
                "result'": 872358977,
                "$cond'": true,
                "exponent'": 36,
                "base": 75,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 872358977,
                "result'": 1002413835,
                "$cond'": true,
                "exponent'": 35,
                "base": 75,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1002413835,
                "result'": 1002413835,
                "$cond'": true,
                "exponent'": 35,
                "base": 75,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1002413835,
                "result'": -2128373703,
                "$cond'": true,
                "exponent'": 34,
                "base": 75,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2128373703,
                "result'": -2128373703,
                "$cond'": true,
                "exponent'": 34,
                "base": 75,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2128373703,
                "result'": -714237773,
                "$cond'": true,
                "exponent'": 33,
                "base": 75,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -714237773,
                "result'": -714237773,
                "$cond'": true,
                "exponent'": 33,
                "base": 75,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -714237773,
                "result'": -2028225423,
                "$cond'": true,
                "exponent'": 32,
                "base": 75,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2028225423,
                "result'": -2028225423,
                "$cond'": true,
                "exponent'": 32,
                "base": 75,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2028225423,
                "result'": -1793051365,
                "$cond'": true,
                "exponent'": 31,
                "base": 75,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1793051365,
                "result'": -1793051365,
                "$cond'": true,
                "exponent'": 31,
                "base": 75,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1793051365,
                "result'": -1334866199,
                "$cond'": true,
                "exponent'": 30,
                "base": 75,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1334866199,
                "result'": -1334866199,
                "$cond'": true,
                "exponent'": 30,
                "base": 75,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1334866199,
                "result'": -1330717117,
                "$cond'": true,
                "exponent'": 29,
                "base": 75,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1330717117,
                "result'": -1330717117,
                "$cond'": true,
                "exponent'": 29,
                "base": 75,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1330717117,
                "result'": -1019535967,
                "$cond'": true,
                "exponent'": 28,
                "base": 75,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1019535967,
                "result'": -1019535967,
                "$cond'": true,
                "exponent'": 28,
                "base": 75,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1019535967,
                "result'": 844213803,
                "$cond'": true,
                "exponent'": 27,
                "base": 75,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 844213803,
                "result'": 844213803,
                "$cond'": true,
                "exponent'": 27,
                "base": 75,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 844213803,
                "result'": -1108474215,
                "$cond'": true,
                "exponent'": 26,
                "base": 75,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1108474215,
                "result'": -1108474215,
                "$cond'": true,
                "exponent'": 26,
                "base": 75,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1108474215,
                "result'": -1531187501,
                "$cond'": true,
                "exponent'": 25,
                "base": 75,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1531187501,
                "result'": -1531187501,
                "$cond'": true,
                "exponent'": 25,
                "base": 75,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1531187501,
                "result'": 1125054417,
                "$cond'": true,
                "exponent'": 24,
                "base": 75,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1125054417,
                "result'": 1125054417,
                "$cond'": true,
                "exponent'": 24,
                "base": 75,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1125054417,
                "result'": -1520264645,
                "$cond'": true,
                "exponent'": 23,
                "base": 75,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1520264645,
                "result'": -1520264645,
                "$cond'": true,
                "exponent'": 23,
                "base": 75,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1520264645,
                "result'": 1944268617,
                "$cond'": true,
                "exponent'": 22,
                "base": 75,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1944268617,
                "result'": 1944268617,
                "$cond'": true,
                "exponent'": 22,
                "base": 75,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1944268617,
                "result'": -208741789,
                "$cond'": true,
                "exponent'": 21,
                "base": 75,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -208741789,
                "result'": -208741789,
                "$cond'": true,
                "exponent'": 21,
                "base": 75,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -208741789,
                "result'": 1524235009,
                "$cond'": true,
                "exponent'": 20,
                "base": 75,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1524235009,
                "result'": 1524235009,
                "$cond'": true,
                "exponent'": 20,
                "base": 75,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1524235009,
                "result'": -1646491317,
                "$cond'": true,
                "exponent'": 19,
                "base": 75,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1646491317,
                "result'": -1646491317,
                "$cond'": true,
                "exponent'": 19,
                "base": 75,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1646491317,
                "result'": 1067202809,
                "$cond'": true,
                "exponent'": 18,
                "base": 75,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1067202809,
                "result'": 1067202809,
                "$cond'": true,
                "exponent'": 18,
                "base": 75,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1067202809,
                "result'": -1564167949,
                "$cond'": true,
                "exponent'": 17,
                "base": 75,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1564167949,
                "result'": -1564167949,
                "$cond'": true,
                "exponent'": 17,
                "base": 75,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1564167949,
                "result'": -1348479183,
                "$cond'": true,
                "exponent'": 16,
                "base": 75,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1348479183,
                "result'": -1348479183,
                "$cond'": true,
                "exponent'": 16,
                "base": 75,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1348479183,
                "result'": 1943276379,
                "$cond'": true,
                "exponent'": 15,
                "base": 75,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1943276379,
                "result'": 1943276379,
                "$cond'": true,
                "exponent'": 15,
                "base": 75,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1943276379,
                "result'": -283159639,
                "$cond'": true,
                "exponent'": 14,
                "base": 75,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -283159639,
                "result'": -283159639,
                "$cond'": true,
                "exponent'": 14,
                "base": 75,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -283159639,
                "result'": 237863555,
                "$cond'": true,
                "exponent'": 13,
                "base": 75,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 237863555,
                "result'": 237863555,
                "$cond'": true,
                "exponent'": 13,
                "base": 75,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 237863555,
                "result'": 659897441,
                "$cond'": true,
                "exponent'": 12,
                "base": 75,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 659897441,
                "result'": 659897441,
                "$cond'": true,
                "exponent'": 12,
                "base": 75,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 659897441,
                "result'": -2047299477,
                "$cond'": true,
                "exponent'": 11,
                "base": 75,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2047299477,
                "result'": -2047299477,
                "$cond'": true,
                "exponent'": 11,
                "base": 75,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2047299477,
                "result'": 1071361881,
                "$cond'": true,
                "exponent'": 10,
                "base": 75,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1071361881,
                "result'": 1071361881,
                "$cond'": true,
                "exponent'": 10,
                "base": 75,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1071361881,
                "result'": -1252237549,
                "$cond'": true,
                "exponent'": 9,
                "base": 75,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1252237549,
                "result'": -1252237549,
                "$cond'": true,
                "exponent'": 9,
                "base": 75,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1252237549,
                "result'": 571464337,
                "$cond'": true,
                "exponent'": 8,
                "base": 75,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 571464337,
                "result'": 571464337,
                "$cond'": true,
                "exponent'": 8,
                "base": 75,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 571464337,
                "result'": -89847685,
                "$cond'": true,
                "exponent'": 7,
                "base": 75,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -89847685,
                "result'": -89847685,
                "$cond'": true,
                "exponent'": 7,
                "base": 75,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -89847685,
                "result'": 1851358217,
                "$cond'": true,
                "exponent'": 6,
                "base": 75,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1851358217,
                "result'": 1851358217,
                "$cond'": true,
                "exponent'": 6,
                "base": 75,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1851358217,
                "result'": 1412912803,
                "$cond'": true,
                "exponent'": 5,
                "base": 75,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1412912803,
                "result'": 1412912803,
                "$cond'": true,
                "exponent'": 5,
                "base": 75,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1412912803,
                "result'": -1405722175,
                "$cond'": true,
                "exponent'": 4,
                "base": 75,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1405722175,
                "result'": -1405722175,
                "$cond'": true,
                "exponent'": 4,
                "base": 75,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1405722175,
                "result'": 1945019275,
                "$cond'": true,
                "exponent'": 3,
                "base": 75,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1945019275,
                "result'": 1945019275,
                "$cond'": true,
                "exponent'": 3,
                "base": 75,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1945019275,
                "result'": -152442439,
                "$cond'": true,
                "exponent'": 2,
                "base": 75,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -152442439,
                "result'": -152442439,
                "$cond'": true,
                "exponent'": 2,
                "base": 75,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -152442439,
                "result'": 1451718963,
                "$cond'": true,
                "exponent'": 1,
                "base": 75,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1451718963,
                "result'": 1451718963,
                "$cond'": true,
                "exponent'": 1,
                "base": 75,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1451718963,
                "result'": 1504739825,
                "$cond'": true,
                "exponent'": 0,
                "base": 75,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1504739825,
                "result'": 1504739825,
                "$cond'": false,
                "exponent'": 0,
                "base": 75,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 1504739825,
                "result'": 1504739825,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 1504739825,
                "base": 75,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 4

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[93, 74]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 93,
                "exponent": 74
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 93,
                "exponent": 74,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 93,
                "$cond'": true,
                "exponent'": 73,
                "base": 93,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 93,
                "result'": 93,
                "$cond'": true,
                "exponent'": 73,
                "base": 93,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 93,
                "result'": 8649,
                "$cond'": true,
                "exponent'": 72,
                "base": 93,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 8649,
                "result'": 8649,
                "$cond'": true,
                "exponent'": 72,
                "base": 93,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 8649,
                "result'": 804357,
                "$cond'": true,
                "exponent'": 71,
                "base": 93,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 804357,
                "result'": 804357,
                "$cond'": true,
                "exponent'": 71,
                "base": 93,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 804357,
                "result'": 74805201,
                "$cond'": true,
                "exponent'": 70,
                "base": 93,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 74805201,
                "result'": 74805201,
                "$cond'": true,
                "exponent'": 70,
                "base": 93,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 74805201,
                "result'": -1633050899,
                "$cond'": true,
                "exponent'": 69,
                "base": 93,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1633050899,
                "result'": -1633050899,
                "$cond'": true,
                "exponent'": 69,
                "base": 93,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1633050899,
                "result'": -1549878247,
                "$cond'": true,
                "exponent'": 68,
                "base": 93,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1549878247,
                "result'": -1549878247,
                "$cond'": true,
                "exponent'": 68,
                "base": 93,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1549878247,
                "result'": 1890211093,
                "$cond'": true,
                "exponent'": 67,
                "base": 93,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1890211093,
                "result'": 1890211093,
                "$cond'": true,
                "exponent'": 67,
                "base": 93,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1890211093,
                "result'": -304027487,
                "$cond'": true,
                "exponent'": 66,
                "base": 93,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -304027487,
                "result'": -304027487,
                "$cond'": true,
                "exponent'": 66,
                "base": 93,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -304027487,
                "result'": 1790214781,
                "$cond'": true,
                "exponent'": 65,
                "base": 93,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1790214781,
                "result'": 1790214781,
                "$cond'": true,
                "exponent'": 65,
                "base": 93,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1790214781,
                "result'": -1013749911,
                "$cond'": true,
                "exponent'": 64,
                "base": 93,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1013749911,
                "result'": -1013749911,
                "$cond'": true,
                "exponent'": 64,
                "base": 93,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1013749911,
                "result'": 210538789,
                "$cond'": true,
                "exponent'": 63,
                "base": 93,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 210538789,
                "result'": 210538789,
                "$cond'": true,
                "exponent'": 63,
                "base": 93,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 210538789,
                "result'": -1894729103,
                "$cond'": true,
                "exponent'": 62,
                "base": 93,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1894729103,
                "result'": -1894729103,
                "$cond'": true,
                "exponent'": 62,
                "base": 93,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1894729103,
                "result'": -116147443,
                "$cond'": true,
                "exponent'": 61,
                "base": 93,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -116147443,
                "result'": -116147443,
                "$cond'": true,
                "exponent'": 61,
                "base": 93,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -116147443,
                "result'": 2083189689,
                "$cond'": true,
                "exponent'": 60,
                "base": 93,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2083189689,
                "result'": 2083189689,
                "$cond'": true,
                "exponent'": 60,
                "base": 93,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2083189689,
                "result'": 463112757,
                "$cond'": true,
                "exponent'": 59,
                "base": 93,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 463112757,
                "result'": 463112757,
                "$cond'": true,
                "exponent'": 59,
                "base": 93,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 463112757,
                "result'": 119813441,
                "$cond'": true,
                "exponent'": 58,
                "base": 93,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 119813441,
                "result'": 119813441,
                "$cond'": true,
                "exponent'": 58,
                "base": 93,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 119813441,
                "result'": -1742251875,
                "$cond'": true,
                "exponent'": 57,
                "base": 93,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1742251875,
                "result'": -1742251875,
                "$cond'": true,
                "exponent'": 57,
                "base": 93,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1742251875,
                "result'": 1179332873,
                "$cond'": true,
                "exponent'": 56,
                "base": 93,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1179332873,
                "result'": 1179332873,
                "$cond'": true,
                "exponent'": 56,
                "base": 93,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1179332873,
                "result'": -1991192507,
                "$cond'": true,
                "exponent'": 55,
                "base": 93,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1991192507,
                "result'": -1991192507,
                "$cond'": true,
                "exponent'": 55,
                "base": 93,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1991192507,
                "result'": -497309423,
                "$cond'": true,
                "exponent'": 54,
                "base": 93,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -497309423,
                "result'": -497309423,
                "$cond'": true,
                "exponent'": 54,
                "base": 93,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -497309423,
                "result'": 994863917,
                "$cond'": true,
                "exponent'": 53,
                "base": 93,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 994863917,
                "result'": 994863917,
                "$cond'": true,
                "exponent'": 53,
                "base": 93,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 994863917,
                "result'": -1966936231,
                "$cond'": true,
                "exponent'": 52,
                "base": 93,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1966936231,
                "result'": -1966936231,
                "$cond'": true,
                "exponent'": 52,
                "base": 93,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1966936231,
                "result'": 1758524245,
                "$cond'": true,
                "exponent'": 51,
                "base": 93,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1758524245,
                "result'": 1758524245,
                "$cond'": true,
                "exponent'": 51,
                "base": 93,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1758524245,
                "result'": 333997537,
                "$cond'": true,
                "exponent'": 50,
                "base": 93,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 333997537,
                "result'": 333997537,
                "$cond'": true,
                "exponent'": 50,
                "base": 93,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 333997537,
                "result'": 996999869,
                "$cond'": true,
                "exponent'": 49,
                "base": 93,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 996999869,
                "result'": 996999869,
                "$cond'": true,
                "exponent'": 49,
                "base": 93,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 996999869,
                "result'": -1768292695,
                "$cond'": true,
                "exponent'": 48,
                "base": 93,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1768292695,
                "result'": -1768292695,
                "$cond'": true,
                "exponent'": 48,
                "base": 93,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1768292695,
                "result'": -1242463387,
                "$cond'": true,
                "exponent'": 47,
                "base": 93,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1242463387,
                "result'": -1242463387,
                "$cond'": true,
                "exponent'": 47,
                "base": 93,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1242463387,
                "result'": 415022001,
                "$cond'": true,
                "exponent'": 46,
                "base": 93,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 415022001,
                "result'": 415022001,
                "$cond'": true,
                "exponent'": 46,
                "base": 93,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 415022001,
                "result'": -57659571,
                "$cond'": true,
                "exponent'": 45,
                "base": 93,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -57659571,
                "result'": -57659571,
                "$cond'": true,
                "exponent'": 45,
                "base": 93,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -57659571,
                "result'": -1067372807,
                "$cond'": true,
                "exponent'": 44,
                "base": 93,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1067372807,
                "result'": -1067372807,
                "$cond'": true,
                "exponent'": 44,
                "base": 93,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1067372807,
                "result'": -481423243,
                "$cond'": true,
                "exponent'": 43,
                "base": 93,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -481423243,
                "result'": -481423243,
                "$cond'": true,
                "exponent'": 43,
                "base": 93,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -481423243,
                "result'": -1822688639,
                "$cond'": true,
                "exponent'": 42,
                "base": 93,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1822688639,
                "result'": -1822688639,
                "$cond'": true,
                "exponent'": 42,
                "base": 93,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1822688639,
                "result'": -2006318883,
                "$cond'": true,
                "exponent'": 41,
                "base": 93,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2006318883,
                "result'": -2006318883,
                "$cond'": true,
                "exponent'": 41,
                "base": 93,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2006318883,
                "result'": -1904062391,
                "$cond'": true,
                "exponent'": 40,
                "base": 93,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1904062391,
                "result'": -1904062391,
                "$cond'": true,
                "exponent'": 40,
                "base": 93,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1904062391,
                "result'": -984143227,
                "$cond'": true,
                "exponent'": 39,
                "base": 93,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -984143227,
                "result'": -984143227,
                "$cond'": true,
                "exponent'": 39,
                "base": 93,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -984143227,
                "result'": -1331006895,
                "$cond'": true,
                "exponent'": 38,
                "base": 93,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1331006895,
                "result'": -1331006895,
                "$cond'": true,
                "exponent'": 38,
                "base": 93,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1331006895,
                "result'": 770410349,
                "$cond'": true,
                "exponent'": 37,
                "base": 93,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 770410349,
                "result'": 770410349,
                "$cond'": true,
                "exponent'": 37,
                "base": 93,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 770410349,
                "result'": -1366281575,
                "$cond'": true,
                "exponent'": 36,
                "base": 93,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1366281575,
                "result'": -1366281575,
                "$cond'": true,
                "exponent'": 36,
                "base": 93,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1366281575,
                "result'": 1784832405,
                "$cond'": true,
                "exponent'": 35,
                "base": 93,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1784832405,
                "result'": 1784832405,
                "$cond'": true,
                "exponent'": 35,
                "base": 93,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1784832405,
                "result'": -1514310879,
                "$cond'": true,
                "exponent'": 34,
                "base": 93,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1514310879,
                "result'": -1514310879,
                "$cond'": true,
                "exponent'": 34,
                "base": 93,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1514310879,
                "result'": 903009021,
                "$cond'": true,
                "exponent'": 33,
                "base": 93,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 903009021,
                "result'": 903009021,
                "$cond'": true,
                "exponent'": 33,
                "base": 93,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 903009021,
                "result'": -1919506967,
                "$cond'": true,
                "exponent'": 32,
                "base": 93,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1919506967,
                "result'": -1919506967,
                "$cond'": true,
                "exponent'": 32,
                "base": 93,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1919506967,
                "result'": 1874478501,
                "$cond'": true,
                "exponent'": 31,
                "base": 93,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1874478501,
                "result'": 1874478501,
                "$cond'": true,
                "exponent'": 31,
                "base": 93,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1874478501,
                "result'": -1767158543,
                "$cond'": true,
                "exponent'": 30,
                "base": 93,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1767158543,
                "result'": -1767158543,
                "$cond'": true,
                "exponent'": 30,
                "base": 93,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1767158543,
                "result'": -1136987251,
                "$cond'": true,
                "exponent'": 29,
                "base": 93,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1136987251,
                "result'": -1136987251,
                "$cond'": true,
                "exponent'": 29,
                "base": 93,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1136987251,
                "result'": 1634368057,
                "$cond'": true,
                "exponent'": 28,
                "base": 93,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1634368057,
                "result'": 1634368057,
                "$cond'": true,
                "exponent'": 28,
                "base": 93,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1634368057,
                "result'": 1672373941,
                "$cond'": true,
                "exponent'": 27,
                "base": 93,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1672373941,
                "result'": 1672373941,
                "$cond'": true,
                "exponent'": 27,
                "base": 93,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1672373941,
                "result'": 911953857,
                "$cond'": true,
                "exponent'": 26,
                "base": 93,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 911953857,
                "result'": 911953857,
                "$cond'": true,
                "exponent'": 26,
                "base": 93,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 911953857,
                "result'": -1087637219,
                "$cond'": true,
                "exponent'": 25,
                "base": 93,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1087637219,
                "result'": -1087637219,
                "$cond'": true,
                "exponent'": 25,
                "base": 93,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1087637219,
                "result'": 1928953737,
                "$cond'": true,
                "exponent'": 24,
                "base": 93,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1928953737,
                "result'": 1928953737,
                "$cond'": true,
                "exponent'": 24,
                "base": 93,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1928953737,
                "result'": -995928891,
                "$cond'": true,
                "exponent'": 23,
                "base": 93,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -995928891,
                "result'": -995928891,
                "$cond'": true,
                "exponent'": 23,
                "base": 93,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -995928891,
                "result'": 1867893649,
                "$cond'": true,
                "exponent'": 22,
                "base": 93,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1867893649,
                "result'": 1867893649,
                "$cond'": true,
                "exponent'": 22,
                "base": 93,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1867893649,
                "result'": 1915417517,
                "$cond'": true,
                "exponent'": 21,
                "base": 93,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1915417517,
                "result'": 1915417517,
                "$cond'": true,
                "exponent'": 21,
                "base": 93,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1915417517,
                "result'": 2040169945,
                "$cond'": true,
                "exponent'": 20,
                "base": 93,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2040169945,
                "result'": 2040169945,
                "$cond'": true,
                "exponent'": 20,
                "base": 93,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2040169945,
                "result'": 757243861,
                "$cond'": true,
                "exponent'": 19,
                "base": 93,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 757243861,
                "result'": 757243861,
                "$cond'": true,
                "exponent'": 19,
                "base": 93,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 757243861,
                "result'": 1704202337,
                "$cond'": true,
                "exponent'": 18,
                "base": 93,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1704202337,
                "result'": 1704202337,
                "$cond'": true,
                "exponent'": 18,
                "base": 93,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1704202337,
                "result'": -422972611,
                "$cond'": true,
                "exponent'": 17,
                "base": 93,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -422972611,
                "result'": -422972611,
                "$cond'": true,
                "exponent'": 17,
                "base": 93,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -422972611,
                "result'": -681747159,
                "$cond'": true,
                "exponent'": 16,
                "base": 93,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -681747159,
                "result'": -681747159,
                "$cond'": true,
                "exponent'": 16,
                "base": 93,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -681747159,
                "result'": 1022023653,
                "$cond'": true,
                "exponent'": 15,
                "base": 93,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1022023653,
                "result'": 1022023653,
                "$cond'": true,
                "exponent'": 15,
                "base": 93,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1022023653,
                "result'": 558919217,
                "$cond'": true,
                "exponent'": 14,
                "base": 93,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 558919217,
                "result'": 558919217,
                "$cond'": true,
                "exponent'": 14,
                "base": 93,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 558919217,
                "result'": 439879629,
                "$cond'": true,
                "exponent'": 13,
                "base": 93,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 439879629,
                "result'": 439879629,
                "$cond'": true,
                "exponent'": 13,
                "base": 93,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 439879629,
                "result'": -2040867463,
                "$cond'": true,
                "exponent'": 12,
                "base": 93,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2040867463,
                "result'": -2040867463,
                "$cond'": true,
                "exponent'": 12,
                "base": 93,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2040867463,
                "result'": -822113035,
                "$cond'": true,
                "exponent'": 11,
                "base": 93,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -822113035,
                "result'": -822113035,
                "$cond'": true,
                "exponent'": 11,
                "base": 93,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -822113035,
                "result'": 852899073,
                "$cond'": true,
                "exponent'": 10,
                "base": 93,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 852899073,
                "result'": 852899073,
                "$cond'": true,
                "exponent'": 10,
                "base": 93,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 852899073,
                "result'": 2010202461,
                "$cond'": true,
                "exponent'": 9,
                "base": 93,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2010202461,
                "result'": 2010202461,
                "$cond'": true,
                "exponent'": 9,
                "base": 93,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2010202461,
                "result'": -2029732151,
                "$cond'": true,
                "exponent'": 8,
                "base": 93,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2029732151,
                "result'": -2029732151,
                "$cond'": true,
                "exponent'": 8,
                "base": 93,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2029732151,
                "result'": 213470981,
                "$cond'": true,
                "exponent'": 7,
                "base": 93,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 213470981,
                "result'": 213470981,
                "$cond'": true,
                "exponent'": 7,
                "base": 93,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 213470981,
                "result'": -1622035247,
                "$cond'": true,
                "exponent'": 6,
                "base": 93,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1622035247,
                "result'": -1622035247,
                "$cond'": true,
                "exponent'": 6,
                "base": 93,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1622035247,
                "result'": -525422611,
                "$cond'": true,
                "exponent'": 5,
                "base": 93,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -525422611,
                "result'": -525422611,
                "$cond'": true,
                "exponent'": 5,
                "base": 93,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -525422611,
                "result'": -1619662567,
                "$cond'": true,
                "exponent'": 4,
                "base": 93,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1619662567,
                "result'": -1619662567,
                "$cond'": true,
                "exponent'": 4,
                "base": 93,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1619662567,
                "result'": -304763371,
                "$cond'": true,
                "exponent'": 3,
                "base": 93,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -304763371,
                "result'": -304763371,
                "$cond'": true,
                "exponent'": 3,
                "base": 93,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -304763371,
                "result'": 1721777569,
                "$cond'": true,
                "exponent'": 2,
                "base": 93,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1721777569,
                "result'": 1721777569,
                "$cond'": true,
                "exponent'": 2,
                "base": 93,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1721777569,
                "result'": 1211523965,
                "$cond'": true,
                "exponent'": 1,
                "base": 93,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1211523965,
                "result'": 1211523965,
                "$cond'": true,
                "exponent'": 1,
                "base": 93,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1211523965,
                "result'": 1002579049,
                "$cond'": true,
                "exponent'": 0,
                "base": 93,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1002579049,
                "result'": 1002579049,
                "$cond'": false,
                "exponent'": 0,
                "base": 93,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 1002579049,
                "result'": 1002579049,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 1002579049,
                "base": 93,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 5

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[62, 84]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 62,
                "exponent": 84
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 62,
                "exponent": 84,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 62,
                "$cond'": true,
                "exponent'": 83,
                "base": 62,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 62,
                "result'": 62,
                "$cond'": true,
                "exponent'": 83,
                "base": 62,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 62,
                "result'": 3844,
                "$cond'": true,
                "exponent'": 82,
                "base": 62,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 3844,
                "result'": 3844,
                "$cond'": true,
                "exponent'": 82,
                "base": 62,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 3844,
                "result'": 238328,
                "$cond'": true,
                "exponent'": 81,
                "base": 62,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 238328,
                "result'": 238328,
                "$cond'": true,
                "exponent'": 81,
                "base": 62,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 238328,
                "result'": 14776336,
                "$cond'": true,
                "exponent'": 80,
                "base": 62,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 14776336,
                "result'": 14776336,
                "$cond'": true,
                "exponent'": 80,
                "base": 62,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 14776336,
                "result'": 916132832,
                "$cond'": true,
                "exponent'": 79,
                "base": 62,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 916132832,
                "result'": 916132832,
                "$cond'": true,
                "exponent'": 79,
                "base": 62,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 916132832,
                "result'": 965660736,
                "$cond'": true,
                "exponent'": 78,
                "base": 62,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 965660736,
                "result'": 965660736,
                "$cond'": true,
                "exponent'": 78,
                "base": 62,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 965660736,
                "result'": -258576512,
                "$cond'": true,
                "exponent'": 77,
                "base": 62,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -258576512,
                "result'": -258576512,
                "$cond'": true,
                "exponent'": 77,
                "base": 62,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -258576512,
                "result'": 1148125440,
                "$cond'": true,
                "exponent'": 76,
                "base": 62,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1148125440,
                "result'": 1148125440,
                "$cond'": true,
                "exponent'": 76,
                "base": 62,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1148125440,
                "result'": -1830666752,
                "$cond'": true,
                "exponent'": 75,
                "base": 62,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1830666752,
                "result'": -1830666752,
                "$cond'": true,
                "exponent'": 75,
                "base": 62,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1830666752,
                "result'": -1832188928,
                "$cond'": true,
                "exponent'": 74,
                "base": 62,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1832188928,
                "result'": -1832188928,
                "$cond'": true,
                "exponent'": 74,
                "base": 62,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1832188928,
                "result'": -1926563840,
                "$cond'": true,
                "exponent'": 73,
                "base": 62,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1926563840,
                "result'": -1926563840,
                "$cond'": true,
                "exponent'": 73,
                "base": 62,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1926563840,
                "result'": 812126208,
                "$cond'": true,
                "exponent'": 72,
                "base": 62,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 812126208,
                "result'": 812126208,
                "$cond'": true,
                "exponent'": 72,
                "base": 62,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 812126208,
                "result'": -1187782656,
                "$cond'": true,
                "exponent'": 71,
                "base": 62,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1187782656,
                "result'": -1187782656,
                "$cond'": true,
                "exponent'": 71,
                "base": 62,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1187782656,
                "result'": -628080640,
                "$cond'": true,
                "exponent'": 70,
                "base": 62,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -628080640,
                "result'": -628080640,
                "$cond'": true,
                "exponent'": 70,
                "base": 62,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -628080640,
                "result'": -286294016,
                "$cond'": true,
                "exponent'": 69,
                "base": 62,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -286294016,
                "result'": -286294016,
                "$cond'": true,
                "exponent'": 69,
                "base": 62,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -286294016,
                "result'": -570359808,
                "$cond'": true,
                "exponent'": 68,
                "base": 62,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -570359808,
                "result'": -570359808,
                "$cond'": true,
                "exponent'": 68,
                "base": 62,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -570359808,
                "result'": -1002569728,
                "$cond'": true,
                "exponent'": 67,
                "base": 62,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1002569728,
                "result'": -1002569728,
                "$cond'": true,
                "exponent'": 67,
                "base": 62,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1002569728,
                "result'": -2029780992,
                "$cond'": true,
                "exponent'": 66,
                "base": 62,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2029780992,
                "result'": -2029780992,
                "$cond'": true,
                "exponent'": 66,
                "base": 62,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2029780992,
                "result'": -1292369920,
                "$cond'": true,
                "exponent'": 65,
                "base": 62,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1292369920,
                "result'": -1292369920,
                "$cond'": true,
                "exponent'": 65,
                "base": 62,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1292369920,
                "result'": 1477443584,
                "$cond'": true,
                "exponent'": 64,
                "base": 62,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1477443584,
                "result'": 1477443584,
                "$cond'": true,
                "exponent'": 64,
                "base": 62,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1477443584,
                "result'": 1407188992,
                "$cond'": true,
                "exponent'": 63,
                "base": 62,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1407188992,
                "result'": 1407188992,
                "$cond'": true,
                "exponent'": 63,
                "base": 62,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1407188992,
                "result'": 1346371584,
                "$cond'": true,
                "exponent'": 62,
                "base": 62,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1346371584,
                "result'": 1346371584,
                "$cond'": true,
                "exponent'": 62,
                "base": 62,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1346371584,
                "result'": 1870659584,
                "$cond'": true,
                "exponent'": 61,
                "base": 62,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1870659584,
                "result'": 1870659584,
                "$cond'": true,
                "exponent'": 61,
                "base": 62,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1870659584,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 60,
                "base": 62,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 16777216,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 60,
                "base": 62,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 16777216,
                "result'": 1040187392,
                "$cond'": true,
                "exponent'": 59,
                "base": 62,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1040187392,
                "result'": 1040187392,
                "$cond'": true,
                "exponent'": 59,
                "base": 62,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1040187392,
                "result'": 67108864,
                "$cond'": true,
                "exponent'": 58,
                "base": 62,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 67108864,
                "result'": 67108864,
                "$cond'": true,
                "exponent'": 58,
                "base": 62,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 67108864,
                "result'": -134217728,
                "$cond'": true,
                "exponent'": 57,
                "base": 62,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -134217728,
                "result'": -134217728,
                "$cond'": true,
                "exponent'": 57,
                "base": 62,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -134217728,
                "result'": 268435456,
                "$cond'": true,
                "exponent'": 56,
                "base": 62,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 268435456,
                "result'": 268435456,
                "$cond'": true,
                "exponent'": 56,
                "base": 62,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 268435456,
                "result'": -536870912,
                "$cond'": true,
                "exponent'": 55,
                "base": 62,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -536870912,
                "result'": -536870912,
                "$cond'": true,
                "exponent'": 55,
                "base": 62,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -536870912,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 54,
                "base": 62,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1073741824,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 54,
                "base": 62,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1073741824,
                "result'": -2147483648,
                "$cond'": true,
                "exponent'": 53,
                "base": 62,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2147483648,
                "result'": -2147483648,
                "$cond'": true,
                "exponent'": 53,
                "base": 62,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2147483648,
                "result'": 0,
                "$cond'": true,
                "exponent'": 52,
                "base": 62,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 52,
                "base": 62,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 51,
                "base": 62,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 51,
                "base": 62,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 50,
                "base": 62,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 50,
                "base": 62,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 49,
                "base": 62,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 49,
                "base": 62,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 48,
                "base": 62,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 48,
                "base": 62,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 47,
                "base": 62,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 47,
                "base": 62,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 46,
                "base": 62,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 46,
                "base": 62,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 45,
                "base": 62,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 45,
                "base": 62,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 44,
                "base": 62,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 44,
                "base": 62,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 62,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 62,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 62,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 62,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 62,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 62,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 62,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 62,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 62,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 62,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 62,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 62,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 62,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 62,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 62,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 62,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 62,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 62,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 62,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 62,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 62,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 62,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 62,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 62,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 62,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 62,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 62,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 62,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 62,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 62,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 62,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 62,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 62,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 62,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 62,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 62,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 62,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 62,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 62,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 62,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 62,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 62,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 62,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 62,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 62,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 62,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 62,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 62,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 62,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 62,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 62,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 62,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 62,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 62,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 62,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 62,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 62,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 62,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 62,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 62,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 62,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 62,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 62,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 62,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 62,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 62,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 62,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 62,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 62,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 62,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 62,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 62,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 62,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 62,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 62,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 62,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 62,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 62,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 62,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 62,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 62,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 62,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 62,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 62,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 62,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 62,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 0,
                "base": 62,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "base": 62,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 0,
                "base": 62,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 6

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[11, 20]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 11,
                "exponent": 20
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 11,
                "exponent": 20,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 11,
                "$cond'": true,
                "exponent'": 19,
                "base": 11,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 11,
                "result'": 11,
                "$cond'": true,
                "exponent'": 19,
                "base": 11,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 11,
                "result'": 121,
                "$cond'": true,
                "exponent'": 18,
                "base": 11,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 121,
                "result'": 121,
                "$cond'": true,
                "exponent'": 18,
                "base": 11,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 121,
                "result'": 1331,
                "$cond'": true,
                "exponent'": 17,
                "base": 11,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1331,
                "result'": 1331,
                "$cond'": true,
                "exponent'": 17,
                "base": 11,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1331,
                "result'": 14641,
                "$cond'": true,
                "exponent'": 16,
                "base": 11,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 14641,
                "result'": 14641,
                "$cond'": true,
                "exponent'": 16,
                "base": 11,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 14641,
                "result'": 161051,
                "$cond'": true,
                "exponent'": 15,
                "base": 11,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 161051,
                "result'": 161051,
                "$cond'": true,
                "exponent'": 15,
                "base": 11,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 161051,
                "result'": 1771561,
                "$cond'": true,
                "exponent'": 14,
                "base": 11,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1771561,
                "result'": 1771561,
                "$cond'": true,
                "exponent'": 14,
                "base": 11,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1771561,
                "result'": 19487171,
                "$cond'": true,
                "exponent'": 13,
                "base": 11,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 19487171,
                "result'": 19487171,
                "$cond'": true,
                "exponent'": 13,
                "base": 11,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 19487171,
                "result'": 214358881,
                "$cond'": true,
                "exponent'": 12,
                "base": 11,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 214358881,
                "result'": 214358881,
                "$cond'": true,
                "exponent'": 12,
                "base": 11,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 214358881,
                "result'": -1937019605,
                "$cond'": true,
                "exponent'": 11,
                "base": 11,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1937019605,
                "result'": -1937019605,
                "$cond'": true,
                "exponent'": 11,
                "base": 11,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1937019605,
                "result'": 167620825,
                "$cond'": true,
                "exponent'": 10,
                "base": 11,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 167620825,
                "result'": 167620825,
                "$cond'": true,
                "exponent'": 10,
                "base": 11,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 167620825,
                "result'": 1843829075,
                "$cond'": true,
                "exponent'": 9,
                "base": 11,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1843829075,
                "result'": 1843829075,
                "$cond'": true,
                "exponent'": 9,
                "base": 11,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1843829075,
                "result'": -1192716655,
                "$cond'": true,
                "exponent'": 8,
                "base": 11,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1192716655,
                "result'": -1192716655,
                "$cond'": true,
                "exponent'": 8,
                "base": 11,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1192716655,
                "result'": -234981317,
                "$cond'": true,
                "exponent'": 7,
                "base": 11,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -234981317,
                "result'": -234981317,
                "$cond'": true,
                "exponent'": 7,
                "base": 11,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -234981317,
                "result'": 1710172809,
                "$cond'": true,
                "exponent'": 6,
                "base": 11,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1710172809,
                "result'": 1710172809,
                "$cond'": true,
                "exponent'": 6,
                "base": 11,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1710172809,
                "result'": 1632031715,
                "$cond'": true,
                "exponent'": 5,
                "base": 11,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1632031715,
                "result'": 1632031715,
                "$cond'": true,
                "exponent'": 5,
                "base": 11,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1632031715,
                "result'": 772479681,
                "$cond'": true,
                "exponent'": 4,
                "base": 11,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 772479681,
                "result'": 772479681,
                "$cond'": true,
                "exponent'": 4,
                "base": 11,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 772479681,
                "result'": -92658101,
                "$cond'": true,
                "exponent'": 3,
                "base": 11,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -92658101,
                "result'": -92658101,
                "$cond'": true,
                "exponent'": 3,
                "base": 11,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -92658101,
                "result'": -1019239111,
                "$cond'": true,
                "exponent'": 2,
                "base": 11,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1019239111,
                "result'": -1019239111,
                "$cond'": true,
                "exponent'": 2,
                "base": 11,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1019239111,
                "result'": 1673271667,
                "$cond'": true,
                "exponent'": 1,
                "base": 11,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1673271667,
                "result'": 1673271667,
                "$cond'": true,
                "exponent'": 1,
                "base": 11,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1673271667,
                "result'": 1226119153,
                "$cond'": true,
                "exponent'": 0,
                "base": 11,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1226119153,
                "result'": 1226119153,
                "$cond'": false,
                "exponent'": 0,
                "base": 11,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 1226119153,
                "result'": 1226119153,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 1226119153,
                "base": 11,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 7

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[85, 50]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 85,
                "exponent": 50
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 85,
                "exponent": 50,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 85,
                "$cond'": true,
                "exponent'": 49,
                "base": 85,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 85,
                "result'": 85,
                "$cond'": true,
                "exponent'": 49,
                "base": 85,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 85,
                "result'": 7225,
                "$cond'": true,
                "exponent'": 48,
                "base": 85,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 7225,
                "result'": 7225,
                "$cond'": true,
                "exponent'": 48,
                "base": 85,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 7225,
                "result'": 614125,
                "$cond'": true,
                "exponent'": 47,
                "base": 85,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 614125,
                "result'": 614125,
                "$cond'": true,
                "exponent'": 47,
                "base": 85,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 614125,
                "result'": 52200625,
                "$cond'": true,
                "exponent'": 46,
                "base": 85,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 52200625,
                "result'": 52200625,
                "$cond'": true,
                "exponent'": 46,
                "base": 85,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 52200625,
                "result'": 142085829,
                "$cond'": true,
                "exponent'": 45,
                "base": 85,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 142085829,
                "result'": 142085829,
                "$cond'": true,
                "exponent'": 45,
                "base": 85,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 142085829,
                "result'": -807606423,
                "$cond'": true,
                "exponent'": 44,
                "base": 85,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -807606423,
                "result'": -807606423,
                "$cond'": true,
                "exponent'": 44,
                "base": 85,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -807606423,
                "result'": 72930781,
                "$cond'": true,
                "exponent'": 43,
                "base": 85,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 72930781,
                "result'": 72930781,
                "$cond'": true,
                "exponent'": 43,
                "base": 85,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 72930781,
                "result'": 1904149089,
                "$cond'": true,
                "exponent'": 42,
                "base": 85,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1904149089,
                "result'": 1904149089,
                "$cond'": true,
                "exponent'": 42,
                "base": 85,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1904149089,
                "result'": -1356084683,
                "$cond'": true,
                "exponent'": 41,
                "base": 85,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1356084683,
                "result'": -1356084683,
                "$cond'": true,
                "exponent'": 41,
                "base": 85,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1356084683,
                "result'": 696918937,
                "$cond'": true,
                "exponent'": 40,
                "base": 85,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 696918937,
                "result'": 696918937,
                "$cond'": true,
                "exponent'": 40,
                "base": 85,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 696918937,
                "result'": -891432499,
                "$cond'": true,
                "exponent'": 39,
                "base": 85,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -891432499,
                "result'": -891432499,
                "$cond'": true,
                "exponent'": 39,
                "base": 85,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -891432499,
                "result'": 1537648913,
                "$cond'": true,
                "exponent'": 38,
                "base": 85,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1537648913,
                "result'": 1537648913,
                "$cond'": true,
                "exponent'": 38,
                "base": 85,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1537648913,
                "result'": 1851138725,
                "$cond'": true,
                "exponent'": 37,
                "base": 85,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1851138725,
                "result'": 1851138725,
                "$cond'": true,
                "exponent'": 37,
                "base": 85,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1851138725,
                "result'": -1566998327,
                "$cond'": true,
                "exponent'": 36,
                "base": 85,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1566998327,
                "result'": -1566998327,
                "$cond'": true,
                "exponent'": 36,
                "base": 85,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1566998327,
                "result'": -50871619,
                "$cond'": true,
                "exponent'": 35,
                "base": 85,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -50871619,
                "result'": -50871619,
                "$cond'": true,
                "exponent'": 35,
                "base": 85,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -50871619,
                "result'": -29120319,
                "$cond'": true,
                "exponent'": 34,
                "base": 85,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -29120319,
                "result'": -29120319,
                "$cond'": true,
                "exponent'": 34,
                "base": 85,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -29120319,
                "result'": 1819740181,
                "$cond'": true,
                "exponent'": 33,
                "base": 85,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1819740181,
                "result'": 1819740181,
                "$cond'": true,
                "exponent'": 33,
                "base": 85,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1819740181,
                "result'": 59092729,
                "$cond'": true,
                "exponent'": 32,
                "base": 85,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 59092729,
                "result'": 59092729,
                "$cond'": true,
                "exponent'": 32,
                "base": 85,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 59092729,
                "result'": 727914669,
                "$cond'": true,
                "exponent'": 31,
                "base": 85,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 727914669,
                "result'": 727914669,
                "$cond'": true,
                "exponent'": 31,
                "base": 85,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 727914669,
                "result'": 1743204721,
                "$cond'": true,
                "exponent'": 30,
                "base": 85,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1743204721,
                "result'": 1743204721,
                "$cond'": true,
                "exponent'": 30,
                "base": 85,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1743204721,
                "result'": 2143513221,
                "$cond'": true,
                "exponent'": 29,
                "base": 85,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2143513221,
                "result'": 2143513221,
                "$cond'": true,
                "exponent'": 29,
                "base": 85,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2143513221,
                "result'": 1809997353,
                "$cond'": true,
                "exponent'": 28,
                "base": 85,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1809997353,
                "result'": 1809997353,
                "$cond'": true,
                "exponent'": 28,
                "base": 85,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1809997353,
                "result'": -769047651,
                "$cond'": true,
                "exponent'": 27,
                "base": 85,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -769047651,
                "result'": -769047651,
                "$cond'": true,
                "exponent'": 27,
                "base": 85,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -769047651,
                "result'": -944540895,
                "$cond'": true,
                "exponent'": 26,
                "base": 85,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -944540895,
                "result'": -944540895,
                "$cond'": true,
                "exponent'": 26,
                "base": 85,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -944540895,
                "result'": 1318402549,
                "$cond'": true,
                "exponent'": 25,
                "base": 85,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1318402549,
                "result'": 1318402549,
                "$cond'": true,
                "exponent'": 25,
                "base": 85,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1318402549,
                "result'": 395066969,
                "$cond'": true,
                "exponent'": 24,
                "base": 85,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 395066969,
                "result'": 395066969,
                "$cond'": true,
                "exponent'": 24,
                "base": 85,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 395066969,
                "result'": -779046003,
                "$cond'": true,
                "exponent'": 23,
                "base": 85,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -779046003,
                "result'": -779046003,
                "$cond'": true,
                "exponent'": 23,
                "base": 85,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -779046003,
                "result'": -1794400815,
                "$cond'": true,
                "exponent'": 22,
                "base": 85,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1794400815,
                "result'": -1794400815,
                "$cond'": true,
                "exponent'": 22,
                "base": 85,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1794400815,
                "result'": 2094753381,
                "$cond'": true,
                "exponent'": 21,
                "base": 85,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2094753381,
                "result'": 2094753381,
                "$cond'": true,
                "exponent'": 21,
                "base": 85,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2094753381,
                "result'": 1960378249,
                "$cond'": true,
                "exponent'": 20,
                "base": 85,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1960378249,
                "result'": 1960378249,
                "$cond'": true,
                "exponent'": 20,
                "base": 85,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1960378249,
                "result'": -871573379,
                "$cond'": true,
                "exponent'": 19,
                "base": 85,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -871573379,
                "result'": -871573379,
                "$cond'": true,
                "exponent'": 19,
                "base": 85,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -871573379,
                "result'": -1069293183,
                "$cond'": true,
                "exponent'": 18,
                "base": 85,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1069293183,
                "result'": -1069293183,
                "$cond'": true,
                "exponent'": 18,
                "base": 85,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1069293183,
                "result'": -695607339,
                "$cond'": true,
                "exponent'": 17,
                "base": 85,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -695607339,
                "result'": -695607339,
                "$cond'": true,
                "exponent'": 17,
                "base": 85,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -695607339,
                "result'": 1002918329,
                "$cond'": true,
                "exponent'": 16,
                "base": 85,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1002918329,
                "result'": 1002918329,
                "$cond'": true,
                "exponent'": 16,
                "base": 85,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1002918329,
                "result'": -651287955,
                "$cond'": true,
                "exponent'": 15,
                "base": 85,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -651287955,
                "result'": -651287955,
                "$cond'": true,
                "exponent'": 15,
                "base": 85,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -651287955,
                "result'": 475098673,
                "$cond'": true,
                "exponent'": 14,
                "base": 85,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 475098673,
                "result'": 475098673,
                "$cond'": true,
                "exponent'": 14,
                "base": 85,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 475098673,
                "result'": 1728681541,
                "$cond'": true,
                "exponent'": 13,
                "base": 85,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1728681541,
                "result'": 1728681541,
                "$cond'": true,
                "exponent'": 13,
                "base": 85,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1728681541,
                "result'": 909042921,
                "$cond'": true,
                "exponent'": 12,
                "base": 85,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 909042921,
                "result'": 909042921,
                "$cond'": true,
                "exponent'": 12,
                "base": 85,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 909042921,
                "result'": -40763043,
                "$cond'": true,
                "exponent'": 11,
                "base": 85,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -40763043,
                "result'": -40763043,
                "$cond'": true,
                "exponent'": 11,
                "base": 85,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -40763043,
                "result'": 830108641,
                "$cond'": true,
                "exponent'": 10,
                "base": 85,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 830108641,
                "result'": 830108641,
                "$cond'": true,
                "exponent'": 10,
                "base": 85,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 830108641,
                "result'": 1839757749,
                "$cond'": true,
                "exponent'": 9,
                "base": 85,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1839757749,
                "result'": 1839757749,
                "$cond'": true,
                "exponent'": 9,
                "base": 85,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1839757749,
                "result'": 1760586009,
                "$cond'": true,
                "exponent'": 8,
                "base": 85,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1760586009,
                "result'": 1760586009,
                "$cond'": true,
                "exponent'": 8,
                "base": 85,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1760586009,
                "result'": -674044595,
                "$cond'": true,
                "exponent'": 7,
                "base": 85,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -674044595,
                "result'": -674044595,
                "$cond'": true,
                "exponent'": 7,
                "base": 85,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -674044595,
                "result'": -1459215727,
                "$cond'": true,
                "exponent'": 6,
                "base": 85,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1459215727,
                "result'": -1459215727,
                "$cond'": true,
                "exponent'": 6,
                "base": 85,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1459215727,
                "result'": 520714789,
                "$cond'": true,
                "exponent'": 5,
                "base": 85,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 520714789,
                "result'": 520714789,
                "$cond'": true,
                "exponent'": 5,
                "base": 85,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 520714789,
                "result'": 1311084105,
                "$cond'": true,
                "exponent'": 4,
                "base": 85,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1311084105,
                "result'": 1311084105,
                "$cond'": true,
                "exponent'": 4,
                "base": 85,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1311084105,
                "result'": -227000771,
                "$cond'": true,
                "exponent'": 3,
                "base": 85,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -227000771,
                "result'": -227000771,
                "$cond'": true,
                "exponent'": 3,
                "base": 85,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -227000771,
                "result'": -2115196351,
                "$cond'": true,
                "exponent'": 2,
                "base": 85,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2115196351,
                "result'": -2115196351,
                "$cond'": true,
                "exponent'": 2,
                "base": 85,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2115196351,
                "result'": 596936597,
                "$cond'": true,
                "exponent'": 1,
                "base": 85,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 596936597,
                "result'": 596936597,
                "$cond'": true,
                "exponent'": 1,
                "base": 85,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 596936597,
                "result'": -799996807,
                "$cond'": true,
                "exponent'": 0,
                "base": 85,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -799996807,
                "result'": -799996807,
                "$cond'": false,
                "exponent'": 0,
                "base": 85,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": -799996807,
                "result'": -799996807,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": -799996807,
                "base": 85,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 8

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[69, 97]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 69,
                "exponent": 97
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 69,
                "exponent": 97,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 69,
                "$cond'": true,
                "exponent'": 96,
                "base": 69,
                "exponent": 97,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 69,
                "result'": 69,
                "$cond'": true,
                "exponent'": 96,
                "base": 69,
                "exponent": 96,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 69,
                "result'": 4761,
                "$cond'": true,
                "exponent'": 95,
                "base": 69,
                "exponent": 96,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 4761,
                "result'": 4761,
                "$cond'": true,
                "exponent'": 95,
                "base": 69,
                "exponent": 95,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 4761,
                "result'": 328509,
                "$cond'": true,
                "exponent'": 94,
                "base": 69,
                "exponent": 95,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 328509,
                "result'": 328509,
                "$cond'": true,
                "exponent'": 94,
                "base": 69,
                "exponent": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 328509,
                "result'": 22667121,
                "$cond'": true,
                "exponent'": 93,
                "base": 69,
                "exponent": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 22667121,
                "result'": 22667121,
                "$cond'": true,
                "exponent'": 93,
                "base": 69,
                "exponent": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 22667121,
                "result'": 1564031349,
                "$cond'": true,
                "exponent'": 92,
                "base": 69,
                "exponent": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1564031349,
                "result'": 1564031349,
                "$cond'": true,
                "exponent'": 92,
                "base": 69,
                "exponent": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1564031349,
                "result'": 543980681,
                "$cond'": true,
                "exponent'": 91,
                "base": 69,
                "exponent": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 543980681,
                "result'": 543980681,
                "$cond'": true,
                "exponent'": 91,
                "base": 69,
                "exponent": 91,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 543980681,
                "result'": -1120038675,
                "$cond'": true,
                "exponent'": 90,
                "base": 69,
                "exponent": 91,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1120038675,
                "result'": -1120038675,
                "$cond'": true,
                "exponent'": 90,
                "base": 69,
                "exponent": 90,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1120038675,
                "result'": 26742753,
                "$cond'": true,
                "exponent'": 89,
                "base": 69,
                "exponent": 90,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 26742753,
                "result'": 26742753,
                "$cond'": true,
                "exponent'": 89,
                "base": 69,
                "exponent": 89,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 26742753,
                "result'": 1845249957,
                "$cond'": true,
                "exponent'": 88,
                "base": 69,
                "exponent": 89,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1845249957,
                "result'": 1845249957,
                "$cond'": true,
                "exponent'": 88,
                "base": 69,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1845249957,
                "result'": -1526771847,
                "$cond'": true,
                "exponent'": 87,
                "base": 69,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1526771847,
                "result'": -1526771847,
                "$cond'": true,
                "exponent'": 87,
                "base": 69,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1526771847,
                "result'": 2026924957,
                "$cond'": true,
                "exponent'": 86,
                "base": 69,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2026924957,
                "result'": 2026924957,
                "$cond'": true,
                "exponent'": 86,
                "base": 69,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2026924957,
                "result'": -1876098735,
                "$cond'": true,
                "exponent'": 85,
                "base": 69,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1876098735,
                "result'": -1876098735,
                "$cond'": true,
                "exponent'": 85,
                "base": 69,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1876098735,
                "result'": -601793835,
                "$cond'": true,
                "exponent'": 84,
                "base": 69,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -601793835,
                "result'": -601793835,
                "$cond'": true,
                "exponent'": 84,
                "base": 69,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -601793835,
                "result'": 1425898345,
                "$cond'": true,
                "exponent'": 83,
                "base": 69,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1425898345,
                "result'": 1425898345,
                "$cond'": true,
                "exponent'": 83,
                "base": 69,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1425898345,
                "result'": -397262003,
                "$cond'": true,
                "exponent'": 82,
                "base": 69,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -397262003,
                "result'": -397262003,
                "$cond'": true,
                "exponent'": 82,
                "base": 69,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -397262003,
                "result'": -1641274431,
                "$cond'": true,
                "exponent'": 81,
                "base": 69,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1641274431,
                "result'": -1641274431,
                "$cond'": true,
                "exponent'": 81,
                "base": 69,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1641274431,
                "result'": -1578786043,
                "$cond'": true,
                "exponent'": 80,
                "base": 69,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1578786043,
                "result'": -1578786043,
                "$cond'": true,
                "exponent'": 80,
                "base": 69,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1578786043,
                "result'": -1562054567,
                "$cond'": true,
                "exponent'": 79,
                "base": 69,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1562054567,
                "result'": -1562054567,
                "$cond'": true,
                "exponent'": 79,
                "base": 69,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1562054567,
                "result'": -407582723,
                "$cond'": true,
                "exponent'": 78,
                "base": 69,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -407582723,
                "result'": -407582723,
                "$cond'": true,
                "exponent'": 78,
                "base": 69,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -407582723,
                "result'": 1941563185,
                "$cond'": true,
                "exponent'": 77,
                "base": 69,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1941563185,
                "result'": 1941563185,
                "$cond'": true,
                "exponent'": 77,
                "base": 69,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1941563185,
                "result'": 823873589,
                "$cond'": true,
                "exponent'": 76,
                "base": 69,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 823873589,
                "result'": 823873589,
                "$cond'": true,
                "exponent'": 76,
                "base": 69,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 823873589,
                "result'": 1012702793,
                "$cond'": true,
                "exponent'": 75,
                "base": 69,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1012702793,
                "result'": 1012702793,
                "$cond'": true,
                "exponent'": 75,
                "base": 69,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1012702793,
                "result'": 1157015981,
                "$cond'": true,
                "exponent'": 74,
                "base": 69,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1157015981,
                "result'": 1157015981,
                "$cond'": true,
                "exponent'": 74,
                "base": 69,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1157015981,
                "result'": -1770275935,
                "$cond'": true,
                "exponent'": 73,
                "base": 69,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1770275935,
                "result'": -1770275935,
                "$cond'": true,
                "exponent'": 73,
                "base": 69,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1770275935,
                "result'": -1889955227,
                "$cond'": true,
                "exponent'": 72,
                "base": 69,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1889955227,
                "result'": -1889955227,
                "$cond'": true,
                "exponent'": 72,
                "base": 69,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1889955227,
                "result'": -1557891783,
                "$cond'": true,
                "exponent'": 71,
                "base": 69,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1557891783,
                "result'": -1557891783,
                "$cond'": true,
                "exponent'": 71,
                "base": 69,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1557891783,
                "result'": -120350627,
                "$cond'": true,
                "exponent'": 70,
                "base": 69,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -120350627,
                "result'": -120350627,
                "$cond'": true,
                "exponent'": 70,
                "base": 69,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -120350627,
                "result'": 285741329,
                "$cond'": true,
                "exponent'": 69,
                "base": 69,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 285741329,
                "result'": 285741329,
                "$cond'": true,
                "exponent'": 69,
                "base": 69,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 285741329,
                "result'": -1758684779,
                "$cond'": true,
                "exponent'": 68,
                "base": 69,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1758684779,
                "result'": -1758684779,
                "$cond'": true,
                "exponent'": 68,
                "base": 69,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1758684779,
                "result'": -1090165463,
                "$cond'": true,
                "exponent'": 67,
                "base": 69,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1090165463,
                "result'": -1090165463,
                "$cond'": true,
                "exponent'": 67,
                "base": 69,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1090165463,
                "result'": 2087994381,
                "$cond'": true,
                "exponent'": 66,
                "base": 69,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2087994381,
                "result'": 2087994381,
                "$cond'": true,
                "exponent'": 66,
                "base": 69,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2087994381,
                "result'": -1957275775,
                "$cond'": true,
                "exponent'": 65,
                "base": 69,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1957275775,
                "result'": -1957275775,
                "$cond'": true,
                "exponent'": 65,
                "base": 69,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1957275775,
                "result'": -1908042299,
                "$cond'": true,
                "exponent'": 64,
                "base": 69,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1908042299,
                "result'": -1908042299,
                "$cond'": true,
                "exponent'": 64,
                "base": 69,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1908042299,
                "result'": 1489067545,
                "$cond'": true,
                "exponent'": 63,
                "base": 69,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1489067545,
                "result'": 1489067545,
                "$cond'": true,
                "exponent'": 63,
                "base": 69,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1489067545,
                "result'": -333554499,
                "$cond'": true,
                "exponent'": 62,
                "base": 69,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -333554499,
                "result'": -333554499,
                "$cond'": true,
                "exponent'": 62,
                "base": 69,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -333554499,
                "result'": -1540423951,
                "$cond'": true,
                "exponent'": 61,
                "base": 69,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1540423951,
                "result'": -1540423951,
                "$cond'": true,
                "exponent'": 61,
                "base": 69,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1540423951,
                "result'": 1084929781,
                "$cond'": true,
                "exponent'": 60,
                "base": 69,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1084929781,
                "result'": 1084929781,
                "$cond'": true,
                "exponent'": 60,
                "base": 69,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1084929781,
                "result'": 1845710857,
                "$cond'": true,
                "exponent'": 59,
                "base": 69,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1845710857,
                "result'": 1845710857,
                "$cond'": true,
                "exponent'": 59,
                "base": 69,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1845710857,
                "result'": -1494969747,
                "$cond'": true,
                "exponent'": 58,
                "base": 69,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1494969747,
                "result'": -1494969747,
                "$cond'": true,
                "exponent'": 58,
                "base": 69,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1494969747,
                "result'": -73697439,
                "$cond'": true,
                "exponent'": 57,
                "base": 69,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -73697439,
                "result'": -73697439,
                "$cond'": true,
                "exponent'": 57,
                "base": 69,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -73697439,
                "result'": -790155995,
                "$cond'": true,
                "exponent'": 56,
                "base": 69,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -790155995,
                "result'": -790155995,
                "$cond'": true,
                "exponent'": 56,
                "base": 69,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -790155995,
                "result'": 1313811193,
                "$cond'": true,
                "exponent'": 55,
                "base": 69,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1313811193,
                "result'": 1313811193,
                "$cond'": true,
                "exponent'": 55,
                "base": 69,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1313811193,
                "result'": 458659101,
                "$cond'": true,
                "exponent'": 54,
                "base": 69,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 458659101,
                "result'": 458659101,
                "$cond'": true,
                "exponent'": 54,
                "base": 69,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 458659101,
                "result'": 1582706897,
                "$cond'": true,
                "exponent'": 53,
                "base": 69,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1582706897,
                "result'": 1582706897,
                "$cond'": true,
                "exponent'": 53,
                "base": 69,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1582706897,
                "result'": 1832593493,
                "$cond'": true,
                "exponent'": 52,
                "base": 69,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1832593493,
                "result'": 1832593493,
                "$cond'": true,
                "exponent'": 52,
                "base": 69,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1832593493,
                "result'": 1894899433,
                "$cond'": true,
                "exponent'": 51,
                "base": 69,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1894899433,
                "result'": 1894899433,
                "$cond'": true,
                "exponent'": 51,
                "base": 69,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1894899433,
                "result'": 1899041997,
                "$cond'": true,
                "exponent'": 50,
                "base": 69,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1899041997,
                "result'": 1899041997,
                "$cond'": true,
                "exponent'": 50,
                "base": 69,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1899041997,
                "result'": -2110088383,
                "$cond'": true,
                "exponent'": 49,
                "base": 69,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2110088383,
                "result'": -2110088383,
                "$cond'": true,
                "exponent'": 49,
                "base": 69,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2110088383,
                "result'": 432789637,
                "$cond'": true,
                "exponent'": 48,
                "base": 69,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 432789637,
                "result'": 432789637,
                "$cond'": true,
                "exponent'": 48,
                "base": 69,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 432789637,
                "result'": -202286119,
                "$cond'": true,
                "exponent'": 47,
                "base": 69,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -202286119,
                "result'": -202286119,
                "$cond'": true,
                "exponent'": 47,
                "base": 69,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -202286119,
                "result'": -1072840323,
                "$cond'": true,
                "exponent'": 46,
                "base": 69,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1072840323,
                "result'": -1072840323,
                "$cond'": true,
                "exponent'": 46,
                "base": 69,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1072840323,
                "result'": -1011538255,
                "$cond'": true,
                "exponent'": 45,
                "base": 69,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1011538255,
                "result'": -1011538255,
                "$cond'": true,
                "exponent'": 45,
                "base": 69,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1011538255,
                "result'": -1076662859,
                "$cond'": true,
                "exponent'": 44,
                "base": 69,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1076662859,
                "result'": -1076662859,
                "$cond'": true,
                "exponent'": 44,
                "base": 69,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1076662859,
                "result'": -1275293239,
                "$cond'": true,
                "exponent'": 43,
                "base": 69,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1275293239,
                "result'": -1275293239,
                "$cond'": true,
                "exponent'": 43,
                "base": 69,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1275293239,
                "result'": -2095887571,
                "$cond'": true,
                "exponent'": 42,
                "base": 69,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2095887571,
                "result'": -2095887571,
                "$cond'": true,
                "exponent'": 42,
                "base": 69,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2095887571,
                "result'": 1412645665,
                "$cond'": true,
                "exponent'": 41,
                "base": 69,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1412645665,
                "result'": 1412645665,
                "$cond'": true,
                "exponent'": 41,
                "base": 69,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1412645665,
                "result'": -1311696923,
                "$cond'": true,
                "exponent'": 40,
                "base": 69,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1311696923,
                "result'": -1311696923,
                "$cond'": true,
                "exponent'": 40,
                "base": 69,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1311696923,
                "result'": -312774471,
                "$cond'": true,
                "exponent'": 39,
                "base": 69,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -312774471,
                "result'": -312774471,
                "$cond'": true,
                "exponent'": 39,
                "base": 69,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -312774471,
                "result'": -106602019,
                "$cond'": true,
                "exponent'": 38,
                "base": 69,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -106602019,
                "result'": -106602019,
                "$cond'": true,
                "exponent'": 38,
                "base": 69,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -106602019,
                "result'": 1234395281,
                "$cond'": true,
                "exponent'": 37,
                "base": 69,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1234395281,
                "result'": 1234395281,
                "$cond'": true,
                "exponent'": 37,
                "base": 69,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1234395281,
                "result'": -726071531,
                "$cond'": true,
                "exponent'": 36,
                "base": 69,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -726071531,
                "result'": -726071531,
                "$cond'": true,
                "exponent'": 36,
                "base": 69,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -726071531,
                "result'": 1440671913,
                "$cond'": true,
                "exponent'": 35,
                "base": 69,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1440671913,
                "result'": 1440671913,
                "$cond'": true,
                "exponent'": 35,
                "base": 69,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1440671913,
                "result'": 622114189,
                "$cond'": true,
                "exponent'": 34,
                "base": 69,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 622114189,
                "result'": 622114189,
                "$cond'": true,
                "exponent'": 34,
                "base": 69,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 622114189,
                "result'": -23793919,
                "$cond'": true,
                "exponent'": 33,
                "base": 69,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -23793919,
                "result'": -23793919,
                "$cond'": true,
                "exponent'": 33,
                "base": 69,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -23793919,
                "result'": -1641780411,
                "$cond'": true,
                "exponent'": 32,
                "base": 69,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1641780411,
                "result'": -1641780411,
                "$cond'": true,
                "exponent'": 32,
                "base": 69,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1641780411,
                "result'": -1613698663,
                "$cond'": true,
                "exponent'": 31,
                "base": 69,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1613698663,
                "result'": -1613698663,
                "$cond'": true,
                "exponent'": 31,
                "base": 69,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1613698663,
                "result'": 323941949,
                "$cond'": true,
                "exponent'": 30,
                "base": 69,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 323941949,
                "result'": 323941949,
                "$cond'": true,
                "exponent'": 30,
                "base": 69,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 323941949,
                "result'": 877158001,
                "$cond'": true,
                "exponent'": 29,
                "base": 69,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 877158001,
                "result'": 877158001,
                "$cond'": true,
                "exponent'": 29,
                "base": 69,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 877158001,
                "result'": 394359925,
                "$cond'": true,
                "exponent'": 28,
                "base": 69,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 394359925,
                "result'": 394359925,
                "$cond'": true,
                "exponent'": 28,
                "base": 69,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 394359925,
                "result'": 1441031049,
                "$cond'": true,
                "exponent'": 27,
                "base": 69,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1441031049,
                "result'": 1441031049,
                "$cond'": true,
                "exponent'": 27,
                "base": 69,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1441031049,
                "result'": 646894573,
                "$cond'": true,
                "exponent'": 26,
                "base": 69,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 646894573,
                "result'": 646894573,
                "$cond'": true,
                "exponent'": 26,
                "base": 69,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 646894573,
                "result'": 1686052577,
                "$cond'": true,
                "exponent'": 25,
                "base": 69,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1686052577,
                "result'": 1686052577,
                "$cond'": true,
                "exponent'": 25,
                "base": 69,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1686052577,
                "result'": 373510821,
                "$cond'": true,
                "exponent'": 24,
                "base": 69,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 373510821,
                "result'": 373510821,
                "$cond'": true,
                "exponent'": 24,
                "base": 69,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 373510821,
                "result'": 2442873,
                "$cond'": true,
                "exponent'": 23,
                "base": 69,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2442873,
                "result'": 2442873,
                "$cond'": true,
                "exponent'": 23,
                "base": 69,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2442873,
                "result'": 168558237,
                "$cond'": true,
                "exponent'": 22,
                "base": 69,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 168558237,
                "result'": 168558237,
                "$cond'": true,
                "exponent'": 22,
                "base": 69,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 168558237,
                "result'": -1254383535,
                "$cond'": true,
                "exponent'": 21,
                "base": 69,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1254383535,
                "result'": -1254383535,
                "$cond'": true,
                "exponent'": 21,
                "base": 69,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1254383535,
                "result'": -653117995,
                "$cond'": true,
                "exponent'": 20,
                "base": 69,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -653117995,
                "result'": -653117995,
                "$cond'": true,
                "exponent'": 20,
                "base": 69,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -653117995,
                "result'": -2115468695,
                "$cond'": true,
                "exponent'": 19,
                "base": 69,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2115468695,
                "result'": -2115468695,
                "$cond'": true,
                "exponent'": 19,
                "base": 69,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2115468695,
                "result'": 61548109,
                "$cond'": true,
                "exponent'": 18,
                "base": 69,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 61548109,
                "result'": 61548109,
                "$cond'": true,
                "exponent'": 18,
                "base": 69,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 61548109,
                "result'": -48147775,
                "$cond'": true,
                "exponent'": 17,
                "base": 69,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -48147775,
                "result'": -48147775,
                "$cond'": true,
                "exponent'": 17,
                "base": 69,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -48147775,
                "result'": 972770821,
                "$cond'": true,
                "exponent'": 16,
                "base": 69,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 972770821,
                "result'": 972770821,
                "$cond'": true,
                "exponent'": 16,
                "base": 69,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 972770821,
                "result'": -1598290087,
                "$cond'": true,
                "exponent'": 15,
                "base": 69,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1598290087,
                "result'": -1598290087,
                "$cond'": true,
                "exponent'": 15,
                "base": 69,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1598290087,
                "result'": 1387133693,
                "$cond'": true,
                "exponent'": 14,
                "base": 69,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1387133693,
                "result'": 1387133693,
                "$cond'": true,
                "exponent'": 14,
                "base": 69,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1387133693,
                "result'": 1222944305,
                "$cond'": true,
                "exponent'": 13,
                "base": 69,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1222944305,
                "result'": 1222944305,
                "$cond'": true,
                "exponent'": 13,
                "base": 69,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1222944305,
                "result'": -1516188875,
                "$cond'": true,
                "exponent'": 12,
                "base": 69,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1516188875,
                "result'": -1516188875,
                "$cond'": true,
                "exponent'": 12,
                "base": 69,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1516188875,
                "result'": -1537817271,
                "$cond'": true,
                "exponent'": 11,
                "base": 69,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1537817271,
                "result'": -1537817271,
                "$cond'": true,
                "exponent'": 11,
                "base": 69,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1537817271,
                "result'": 1264790701,
                "$cond'": true,
                "exponent'": 10,
                "base": 69,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1264790701,
                "result'": 1264790701,
                "$cond'": true,
                "exponent'": 10,
                "base": 69,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1264790701,
                "result'": 1371212449,
                "$cond'": true,
                "exponent'": 9,
                "base": 69,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1371212449,
                "result'": 1371212449,
                "$cond'": true,
                "exponent'": 9,
                "base": 69,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1371212449,
                "result'": 124378469,
                "$cond'": true,
                "exponent'": 8,
                "base": 69,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 124378469,
                "result'": 124378469,
                "$cond'": true,
                "exponent'": 8,
                "base": 69,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 124378469,
                "result'": -7820231,
                "$cond'": true,
                "exponent'": 7,
                "base": 69,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -7820231,
                "result'": -7820231,
                "$cond'": true,
                "exponent'": 7,
                "base": 69,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -7820231,
                "result'": -539595939,
                "$cond'": true,
                "exponent'": 6,
                "base": 69,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -539595939,
                "result'": -539595939,
                "$cond'": true,
                "exponent'": 6,
                "base": 69,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -539595939,
                "result'": 1422585873,
                "$cond'": true,
                "exponent'": 5,
                "base": 69,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1422585873,
                "result'": 1422585873,
                "$cond'": true,
                "exponent'": 5,
                "base": 69,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1422585873,
                "result'": -625822571,
                "$cond'": true,
                "exponent'": 4,
                "base": 69,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -625822571,
                "result'": -625822571,
                "$cond'": true,
                "exponent'": 4,
                "base": 69,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -625822571,
                "result'": -232084439,
                "$cond'": true,
                "exponent'": 3,
                "base": 69,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -232084439,
                "result'": -232084439,
                "$cond'": true,
                "exponent'": 3,
                "base": 69,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -232084439,
                "result'": 1166042893,
                "$cond'": true,
                "exponent'": 2,
                "base": 69,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1166042893,
                "result'": 1166042893,
                "$cond'": true,
                "exponent'": 2,
                "base": 69,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1166042893,
                "result'": -1147419007,
                "$cond'": true,
                "exponent'": 1,
                "base": 69,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1147419007,
                "result'": -1147419007,
                "$cond'": true,
                "exponent'": 1,
                "base": 69,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1147419007,
                "result'": -1862500155,
                "$cond'": true,
                "exponent'": 0,
                "base": 69,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1862500155,
                "result'": -1862500155,
                "$cond'": false,
                "exponent'": 0,
                "base": 69,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": -1862500155,
                "result'": -1862500155,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": -1862500155,
                "base": 69,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 9

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[8, 94]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 8,
                "exponent": 94
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 8,
                "exponent": 94,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 8,
                "$cond'": true,
                "exponent'": 93,
                "base": 8,
                "exponent": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 8,
                "result'": 8,
                "$cond'": true,
                "exponent'": 93,
                "base": 8,
                "exponent": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 8,
                "result'": 64,
                "$cond'": true,
                "exponent'": 92,
                "base": 8,
                "exponent": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 64,
                "result'": 64,
                "$cond'": true,
                "exponent'": 92,
                "base": 8,
                "exponent": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 64,
                "result'": 512,
                "$cond'": true,
                "exponent'": 91,
                "base": 8,
                "exponent": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 512,
                "result'": 512,
                "$cond'": true,
                "exponent'": 91,
                "base": 8,
                "exponent": 91,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 512,
                "result'": 4096,
                "$cond'": true,
                "exponent'": 90,
                "base": 8,
                "exponent": 91,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 4096,
                "result'": 4096,
                "$cond'": true,
                "exponent'": 90,
                "base": 8,
                "exponent": 90,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 4096,
                "result'": 32768,
                "$cond'": true,
                "exponent'": 89,
                "base": 8,
                "exponent": 90,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 32768,
                "result'": 32768,
                "$cond'": true,
                "exponent'": 89,
                "base": 8,
                "exponent": 89,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 32768,
                "result'": 262144,
                "$cond'": true,
                "exponent'": 88,
                "base": 8,
                "exponent": 89,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 262144,
                "result'": 262144,
                "$cond'": true,
                "exponent'": 88,
                "base": 8,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 262144,
                "result'": 2097152,
                "$cond'": true,
                "exponent'": 87,
                "base": 8,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2097152,
                "result'": 2097152,
                "$cond'": true,
                "exponent'": 87,
                "base": 8,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2097152,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 86,
                "base": 8,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 16777216,
                "result'": 16777216,
                "$cond'": true,
                "exponent'": 86,
                "base": 8,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 16777216,
                "result'": 134217728,
                "$cond'": true,
                "exponent'": 85,
                "base": 8,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 134217728,
                "result'": 134217728,
                "$cond'": true,
                "exponent'": 85,
                "base": 8,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 134217728,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 84,
                "base": 8,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1073741824,
                "result'": 1073741824,
                "$cond'": true,
                "exponent'": 84,
                "base": 8,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1073741824,
                "result'": 0,
                "$cond'": true,
                "exponent'": 83,
                "base": 8,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 83,
                "base": 8,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 82,
                "base": 8,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 82,
                "base": 8,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 81,
                "base": 8,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 81,
                "base": 8,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 80,
                "base": 8,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 80,
                "base": 8,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 79,
                "base": 8,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 79,
                "base": 8,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 78,
                "base": 8,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 78,
                "base": 8,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 77,
                "base": 8,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 77,
                "base": 8,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 76,
                "base": 8,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 76,
                "base": 8,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 75,
                "base": 8,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 75,
                "base": 8,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 74,
                "base": 8,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 74,
                "base": 8,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 73,
                "base": 8,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 73,
                "base": 8,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 72,
                "base": 8,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 72,
                "base": 8,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 71,
                "base": 8,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 71,
                "base": 8,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 70,
                "base": 8,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 70,
                "base": 8,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 69,
                "base": 8,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 69,
                "base": 8,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 68,
                "base": 8,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 68,
                "base": 8,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 67,
                "base": 8,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 67,
                "base": 8,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 66,
                "base": 8,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 66,
                "base": 8,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 65,
                "base": 8,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 65,
                "base": 8,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 64,
                "base": 8,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 64,
                "base": 8,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 63,
                "base": 8,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 63,
                "base": 8,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 62,
                "base": 8,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 62,
                "base": 8,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 61,
                "base": 8,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 61,
                "base": 8,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 60,
                "base": 8,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 60,
                "base": 8,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 59,
                "base": 8,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 59,
                "base": 8,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 58,
                "base": 8,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 58,
                "base": 8,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 57,
                "base": 8,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 57,
                "base": 8,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 56,
                "base": 8,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 56,
                "base": 8,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 55,
                "base": 8,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 55,
                "base": 8,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 54,
                "base": 8,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 54,
                "base": 8,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 53,
                "base": 8,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 53,
                "base": 8,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 52,
                "base": 8,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 52,
                "base": 8,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 51,
                "base": 8,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 51,
                "base": 8,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 50,
                "base": 8,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 50,
                "base": 8,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 49,
                "base": 8,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 49,
                "base": 8,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 48,
                "base": 8,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 48,
                "base": 8,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 47,
                "base": 8,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 47,
                "base": 8,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 46,
                "base": 8,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 46,
                "base": 8,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 45,
                "base": 8,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 45,
                "base": 8,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 44,
                "base": 8,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 44,
                "base": 8,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 8,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 43,
                "base": 8,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 8,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 42,
                "base": 8,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 8,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 41,
                "base": 8,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 8,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 40,
                "base": 8,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 8,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 39,
                "base": 8,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 8,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 38,
                "base": 8,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 8,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 37,
                "base": 8,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 8,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 36,
                "base": 8,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 8,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 35,
                "base": 8,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 8,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 34,
                "base": 8,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 8,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 33,
                "base": 8,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 8,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 32,
                "base": 8,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 8,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 31,
                "base": 8,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 8,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 30,
                "base": 8,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 8,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 29,
                "base": 8,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 8,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 28,
                "base": 8,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 8,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 27,
                "base": 8,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 8,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 26,
                "base": 8,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 8,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 25,
                "base": 8,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 8,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 24,
                "base": 8,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 8,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 23,
                "base": 8,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 8,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 22,
                "base": 8,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 8,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 21,
                "base": 8,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 8,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 20,
                "base": 8,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 8,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 19,
                "base": 8,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 8,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 18,
                "base": 8,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 8,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 17,
                "base": 8,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 8,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 16,
                "base": 8,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 8,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 15,
                "base": 8,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 8,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 14,
                "base": 8,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 8,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 13,
                "base": 8,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 8,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 12,
                "base": 8,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 8,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 11,
                "base": 8,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 8,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 10,
                "base": 8,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 8,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 9,
                "base": 8,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 8,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 8,
                "base": 8,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 8,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 7,
                "base": 8,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 8,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 6,
                "base": 8,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 8,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 5,
                "base": 8,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 8,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 4,
                "base": 8,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 8,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 3,
                "base": 8,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 8,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 2,
                "base": 8,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 8,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 1,
                "base": 8,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": true,
                "exponent'": 0,
                "base": 8,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "base": 8,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 0,
                "result'": 0,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 0,
                "base": 8,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 10

### Modified Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[43, 89]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "find_power",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1,
                "base": 43,
                "exponent": 89
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "$cond'": true,
                "base": 43,
                "exponent": 89,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 43,
                "$cond'": true,
                "exponent'": 88,
                "base": 43,
                "exponent": 89,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 43,
                "result'": 43,
                "$cond'": true,
                "exponent'": 88,
                "base": 43,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 43,
                "result'": 1849,
                "$cond'": true,
                "exponent'": 87,
                "base": 43,
                "exponent": 88,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1849,
                "result'": 1849,
                "$cond'": true,
                "exponent'": 87,
                "base": 43,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1849,
                "result'": 79507,
                "$cond'": true,
                "exponent'": 86,
                "base": 43,
                "exponent": 87,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 79507,
                "result'": 79507,
                "$cond'": true,
                "exponent'": 86,
                "base": 43,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 79507,
                "result'": 3418801,
                "$cond'": true,
                "exponent'": 85,
                "base": 43,
                "exponent": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 3418801,
                "result'": 3418801,
                "$cond'": true,
                "exponent'": 85,
                "base": 43,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 3418801,
                "result'": 147008443,
                "$cond'": true,
                "exponent'": 84,
                "base": 43,
                "exponent": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 147008443,
                "result'": 147008443,
                "$cond'": true,
                "exponent'": 84,
                "base": 43,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 147008443,
                "result'": 2026395753,
                "$cond'": true,
                "exponent'": 83,
                "base": 43,
                "exponent": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 2026395753,
                "result'": 2026395753,
                "$cond'": true,
                "exponent'": 83,
                "base": 43,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 2026395753,
                "result'": 1235671459,
                "$cond'": true,
                "exponent'": 82,
                "base": 43,
                "exponent": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1235671459,
                "result'": 1235671459,
                "$cond'": true,
                "exponent'": 82,
                "base": 43,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1235671459,
                "result'": 1594265185,
                "$cond'": true,
                "exponent'": 81,
                "base": 43,
                "exponent": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1594265185,
                "result'": 1594265185,
                "$cond'": true,
                "exponent'": 81,
                "base": 43,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1594265185,
                "result'": -166073781,
                "$cond'": true,
                "exponent'": 80,
                "base": 43,
                "exponent": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -166073781,
                "result'": -166073781,
                "$cond'": true,
                "exponent'": 80,
                "base": 43,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -166073781,
                "result'": 1448762009,
                "$cond'": true,
                "exponent'": 79,
                "base": 43,
                "exponent": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1448762009,
                "result'": 1448762009,
                "$cond'": true,
                "exponent'": 79,
                "base": 43,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1448762009,
                "result'": -2127743053,
                "$cond'": true,
                "exponent'": 78,
                "base": 43,
                "exponent": 79,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2127743053,
                "result'": -2127743053,
                "$cond'": true,
                "exponent'": 78,
                "base": 43,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2127743053,
                "result'": -1298638063,
                "$cond'": true,
                "exponent'": 77,
                "base": 43,
                "exponent": 78,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1298638063,
                "result'": -1298638063,
                "$cond'": true,
                "exponent'": 77,
                "base": 43,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1298638063,
                "result'": -6861861,
                "$cond'": true,
                "exponent'": 76,
                "base": 43,
                "exponent": 77,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -6861861,
                "result'": -6861861,
                "$cond'": true,
                "exponent'": 76,
                "base": 43,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -6861861,
                "result'": -295060023,
                "$cond'": true,
                "exponent'": 75,
                "base": 43,
                "exponent": 76,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -295060023,
                "result'": -295060023,
                "$cond'": true,
                "exponent'": 75,
                "base": 43,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -295060023,
                "result'": 197320899,
                "$cond'": true,
                "exponent'": 74,
                "base": 43,
                "exponent": 75,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 197320899,
                "result'": 197320899,
                "$cond'": true,
                "exponent'": 74,
                "base": 43,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 197320899,
                "result'": -105135935,
                "$cond'": true,
                "exponent'": 73,
                "base": 43,
                "exponent": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -105135935,
                "result'": -105135935,
                "$cond'": true,
                "exponent'": 73,
                "base": 43,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -105135935,
                "result'": -225877909,
                "$cond'": true,
                "exponent'": 72,
                "base": 43,
                "exponent": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -225877909,
                "result'": -225877909,
                "$cond'": true,
                "exponent'": 72,
                "base": 43,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -225877909,
                "result'": -1122815495,
                "$cond'": true,
                "exponent'": 71,
                "base": 43,
                "exponent": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1122815495,
                "result'": -1122815495,
                "$cond'": true,
                "exponent'": 71,
                "base": 43,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1122815495,
                "result'": -1036426029,
                "$cond'": true,
                "exponent'": 70,
                "base": 43,
                "exponent": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1036426029,
                "result'": -1036426029,
                "$cond'": true,
                "exponent'": 70,
                "base": 43,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1036426029,
                "result'": -1616646287,
                "$cond'": true,
                "exponent'": 69,
                "base": 43,
                "exponent": 70,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1616646287,
                "result'": -1616646287,
                "$cond'": true,
                "exponent'": 69,
                "base": 43,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1616646287,
                "result'": -796313605,
                "$cond'": true,
                "exponent'": 68,
                "base": 43,
                "exponent": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -796313605,
                "result'": -796313605,
                "$cond'": true,
                "exponent'": 68,
                "base": 43,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -796313605,
                "result'": 118253353,
                "$cond'": true,
                "exponent'": 67,
                "base": 43,
                "exponent": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 118253353,
                "result'": 118253353,
                "$cond'": true,
                "exponent'": 67,
                "base": 43,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 118253353,
                "result'": 789926883,
                "$cond'": true,
                "exponent'": 66,
                "base": 43,
                "exponent": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 789926883,
                "result'": 789926883,
                "$cond'": true,
                "exponent'": 66,
                "base": 43,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 789926883,
                "result'": -392882399,
                "$cond'": true,
                "exponent'": 65,
                "base": 43,
                "exponent": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -392882399,
                "result'": -392882399,
                "$cond'": true,
                "exponent'": 65,
                "base": 43,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -392882399,
                "result'": 285926027,
                "$cond'": true,
                "exponent'": 64,
                "base": 43,
                "exponent": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 285926027,
                "result'": 285926027,
                "$cond'": true,
                "exponent'": 64,
                "base": 43,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 285926027,
                "result'": -590082727,
                "$cond'": true,
                "exponent'": 63,
                "base": 43,
                "exponent": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -590082727,
                "result'": -590082727,
                "$cond'": true,
                "exponent'": 63,
                "base": 43,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -590082727,
                "result'": 396246515,
                "$cond'": true,
                "exponent'": 62,
                "base": 43,
                "exponent": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 396246515,
                "result'": 396246515,
                "$cond'": true,
                "exponent'": 62,
                "base": 43,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 396246515,
                "result'": -141269039,
                "$cond'": true,
                "exponent'": 61,
                "base": 43,
                "exponent": 62,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -141269039,
                "result'": -141269039,
                "$cond'": true,
                "exponent'": 61,
                "base": 43,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -141269039,
                "result'": -1779601381,
                "$cond'": true,
                "exponent'": 60,
                "base": 43,
                "exponent": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1779601381,
                "result'": -1779601381,
                "$cond'": true,
                "exponent'": 60,
                "base": 43,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1779601381,
                "result'": 786551945,
                "$cond'": true,
                "exponent'": 59,
                "base": 43,
                "exponent": 60,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 786551945,
                "result'": 786551945,
                "$cond'": true,
                "exponent'": 59,
                "base": 43,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 786551945,
                "result'": -538004733,
                "$cond'": true,
                "exponent'": 58,
                "base": 43,
                "exponent": 59,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -538004733,
                "result'": -538004733,
                "$cond'": true,
                "exponent'": 58,
                "base": 43,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -538004733,
                "result'": -1659367039,
                "$cond'": true,
                "exponent'": 57,
                "base": 43,
                "exponent": 58,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1659367039,
                "result'": -1659367039,
                "$cond'": true,
                "exponent'": 57,
                "base": 43,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1659367039,
                "result'": 1661661355,
                "$cond'": true,
                "exponent'": 56,
                "base": 43,
                "exponent": 57,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1661661355,
                "result'": 1661661355,
                "$cond'": true,
                "exponent'": 56,
                "base": 43,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1661661355,
                "result'": -1563005767,
                "$cond'": true,
                "exponent'": 55,
                "base": 43,
                "exponent": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1563005767,
                "result'": -1563005767,
                "$cond'": true,
                "exponent'": 55,
                "base": 43,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1563005767,
                "result'": 1510228755,
                "$cond'": true,
                "exponent'": 54,
                "base": 43,
                "exponent": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1510228755,
                "result'": 1510228755,
                "$cond'": true,
                "exponent'": 54,
                "base": 43,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1510228755,
                "result'": 515327025,
                "$cond'": true,
                "exponent'": 53,
                "base": 43,
                "exponent": 54,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 515327025,
                "result'": 515327025,
                "$cond'": true,
                "exponent'": 53,
                "base": 43,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 515327025,
                "result'": 684225595,
                "$cond'": true,
                "exponent'": 52,
                "base": 43,
                "exponent": 53,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 684225595,
                "result'": 684225595,
                "$cond'": true,
                "exponent'": 52,
                "base": 43,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 684225595,
                "result'": -643070487,
                "$cond'": true,
                "exponent'": 51,
                "base": 43,
                "exponent": 52,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -643070487,
                "result'": -643070487,
                "$cond'": true,
                "exponent'": 51,
                "base": 43,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -643070487,
                "result'": -1882227165,
                "$cond'": true,
                "exponent'": 50,
                "base": 43,
                "exponent": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1882227165,
                "result'": -1882227165,
                "$cond'": true,
                "exponent'": 50,
                "base": 43,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1882227165,
                "result'": 668610529,
                "$cond'": true,
                "exponent'": 49,
                "base": 43,
                "exponent": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 668610529,
                "result'": 668610529,
                "$cond'": true,
                "exponent'": 49,
                "base": 43,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 668610529,
                "result'": -1314518325,
                "$cond'": true,
                "exponent'": 48,
                "base": 43,
                "exponent": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1314518325,
                "result'": -1314518325,
                "$cond'": true,
                "exponent'": 48,
                "base": 43,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1314518325,
                "result'": -689713127,
                "$cond'": true,
                "exponent'": 47,
                "base": 43,
                "exponent": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -689713127,
                "result'": -689713127,
                "$cond'": true,
                "exponent'": 47,
                "base": 43,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -689713127,
                "result'": 407106611,
                "$cond'": true,
                "exponent'": 46,
                "base": 43,
                "exponent": 47,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 407106611,
                "result'": 407106611,
                "$cond'": true,
                "exponent'": 46,
                "base": 43,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 407106611,
                "result'": 325715089,
                "$cond'": true,
                "exponent'": 45,
                "base": 43,
                "exponent": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 325715089,
                "result'": 325715089,
                "$cond'": true,
                "exponent'": 45,
                "base": 43,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 325715089,
                "result'": 1120846939,
                "$cond'": true,
                "exponent'": 44,
                "base": 43,
                "exponent": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1120846939,
                "result'": 1120846939,
                "$cond'": true,
                "exponent'": 44,
                "base": 43,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1120846939,
                "result'": 951778121,
                "$cond'": true,
                "exponent'": 43,
                "base": 43,
                "exponent": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 951778121,
                "result'": 951778121,
                "$cond'": true,
                "exponent'": 43,
                "base": 43,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 951778121,
                "result'": -2023213757,
                "$cond'": true,
                "exponent'": 42,
                "base": 43,
                "exponent": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2023213757,
                "result'": -2023213757,
                "$cond'": true,
                "exponent'": 42,
                "base": 43,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2023213757,
                "result'": -1098845631,
                "$cond'": true,
                "exponent'": 41,
                "base": 43,
                "exponent": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1098845631,
                "result'": -1098845631,
                "$cond'": true,
                "exponent'": 41,
                "base": 43,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1098845631,
                "result'": -5721877,
                "$cond'": true,
                "exponent'": 40,
                "base": 43,
                "exponent": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -5721877,
                "result'": -5721877,
                "$cond'": true,
                "exponent'": 40,
                "base": 43,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -5721877,
                "result'": -246040711,
                "$cond'": true,
                "exponent'": 39,
                "base": 43,
                "exponent": 40,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -246040711,
                "result'": -246040711,
                "$cond'": true,
                "exponent'": 39,
                "base": 43,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -246040711,
                "result'": -1989815981,
                "$cond'": true,
                "exponent'": 38,
                "base": 43,
                "exponent": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1989815981,
                "result'": -1989815981,
                "$cond'": true,
                "exponent'": 38,
                "base": 43,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1989815981,
                "result'": 337258737,
                "$cond'": true,
                "exponent'": 37,
                "base": 43,
                "exponent": 38,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 337258737,
                "result'": 337258737,
                "$cond'": true,
                "exponent'": 37,
                "base": 43,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 337258737,
                "result'": 1617223803,
                "$cond'": true,
                "exponent'": 36,
                "base": 43,
                "exponent": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1617223803,
                "result'": 1617223803,
                "$cond'": true,
                "exponent'": 36,
                "base": 43,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1617223803,
                "result'": 821146793,
                "$cond'": true,
                "exponent'": 35,
                "base": 43,
                "exponent": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 821146793,
                "result'": 821146793,
                "$cond'": true,
                "exponent'": 35,
                "base": 43,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 821146793,
                "result'": 949573731,
                "$cond'": true,
                "exponent'": 34,
                "base": 43,
                "exponent": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 949573731,
                "result'": 949573731,
                "$cond'": true,
                "exponent'": 34,
                "base": 43,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 949573731,
                "result'": -2118002527,
                "$cond'": true,
                "exponent'": 33,
                "base": 43,
                "exponent": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2118002527,
                "result'": -2118002527,
                "$cond'": true,
                "exponent'": 33,
                "base": 43,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2118002527,
                "result'": -879795445,
                "$cond'": true,
                "exponent'": 32,
                "base": 43,
                "exponent": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -879795445,
                "result'": -879795445,
                "$cond'": true,
                "exponent'": 32,
                "base": 43,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -879795445,
                "result'": 823501529,
                "$cond'": true,
                "exponent'": 31,
                "base": 43,
                "exponent": 32,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 823501529,
                "result'": 823501529,
                "$cond'": true,
                "exponent'": 31,
                "base": 43,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 823501529,
                "result'": 1050827379,
                "$cond'": true,
                "exponent'": 30,
                "base": 43,
                "exponent": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1050827379,
                "result'": 1050827379,
                "$cond'": true,
                "exponent'": 30,
                "base": 43,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1050827379,
                "result'": -2059062959,
                "$cond'": true,
                "exponent'": 29,
                "base": 43,
                "exponent": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2059062959,
                "result'": -2059062959,
                "$cond'": true,
                "exponent'": 29,
                "base": 43,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2059062959,
                "result'": 1654605979,
                "$cond'": true,
                "exponent'": 28,
                "base": 43,
                "exponent": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1654605979,
                "result'": 1654605979,
                "$cond'": true,
                "exponent'": 28,
                "base": 43,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1654605979,
                "result'": -1866386935,
                "$cond'": true,
                "exponent'": 27,
                "base": 43,
                "exponent": 28,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1866386935,
                "result'": -1866386935,
                "$cond'": true,
                "exponent'": 27,
                "base": 43,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1866386935,
                "result'": 1349740419,
                "$cond'": true,
                "exponent'": 26,
                "base": 43,
                "exponent": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1349740419,
                "result'": 1349740419,
                "$cond'": true,
                "exponent'": 26,
                "base": 43,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1349740419,
                "result'": -2090704127,
                "$cond'": true,
                "exponent'": 25,
                "base": 43,
                "exponent": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2090704127,
                "result'": -2090704127,
                "$cond'": true,
                "exponent'": 25,
                "base": 43,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2090704127,
                "result'": 294035755,
                "$cond'": true,
                "exponent'": 24,
                "base": 43,
                "exponent": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 294035755,
                "result'": 294035755,
                "$cond'": true,
                "exponent'": 24,
                "base": 43,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 294035755,
                "result'": -241364423,
                "$cond'": true,
                "exponent'": 23,
                "base": 43,
                "exponent": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -241364423,
                "result'": -241364423,
                "$cond'": true,
                "exponent'": 23,
                "base": 43,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -241364423,
                "result'": -1788735597,
                "$cond'": true,
                "exponent'": 22,
                "base": 43,
                "exponent": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1788735597,
                "result'": -1788735597,
                "$cond'": true,
                "exponent'": 22,
                "base": 43,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1788735597,
                "result'": 393780657,
                "$cond'": true,
                "exponent'": 21,
                "base": 43,
                "exponent": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 393780657,
                "result'": 393780657,
                "$cond'": true,
                "exponent'": 21,
                "base": 43,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 393780657,
                "result'": -247300933,
                "$cond'": true,
                "exponent'": 20,
                "base": 43,
                "exponent": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -247300933,
                "result'": -247300933,
                "$cond'": true,
                "exponent'": 20,
                "base": 43,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -247300933,
                "result'": -2044005527,
                "$cond'": true,
                "exponent'": 19,
                "base": 43,
                "exponent": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2044005527,
                "result'": -2044005527,
                "$cond'": true,
                "exponent'": 19,
                "base": 43,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2044005527,
                "result'": -1992891741,
                "$cond'": true,
                "exponent'": 18,
                "base": 43,
                "exponent": 19,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1992891741,
                "result'": -1992891741,
                "$cond'": true,
                "exponent'": 18,
                "base": 43,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1992891741,
                "result'": 205001057,
                "$cond'": true,
                "exponent'": 17,
                "base": 43,
                "exponent": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 205001057,
                "result'": 205001057,
                "$cond'": true,
                "exponent'": 17,
                "base": 43,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 205001057,
                "result'": 225110859,
                "$cond'": true,
                "exponent'": 16,
                "base": 43,
                "exponent": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 225110859,
                "result'": 225110859,
                "$cond'": true,
                "exponent'": 16,
                "base": 43,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 225110859,
                "result'": 1089832345,
                "$cond'": true,
                "exponent'": 15,
                "base": 43,
                "exponent": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1089832345,
                "result'": 1089832345,
                "$cond'": true,
                "exponent'": 15,
                "base": 43,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1089832345,
                "result'": -381849421,
                "$cond'": true,
                "exponent'": 14,
                "base": 43,
                "exponent": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -381849421,
                "result'": -381849421,
                "$cond'": true,
                "exponent'": 14,
                "base": 43,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -381849421,
                "result'": 760344081,
                "$cond'": true,
                "exponent'": 13,
                "base": 43,
                "exponent": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 760344081,
                "result'": 760344081,
                "$cond'": true,
                "exponent'": 13,
                "base": 43,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 760344081,
                "result'": -1664942885,
                "$cond'": true,
                "exponent'": 12,
                "base": 43,
                "exponent": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1664942885,
                "result'": -1664942885,
                "$cond'": true,
                "exponent'": 12,
                "base": 43,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1664942885,
                "result'": 1421899977,
                "$cond'": true,
                "exponent'": 11,
                "base": 43,
                "exponent": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1421899977,
                "result'": 1421899977,
                "$cond'": true,
                "exponent'": 11,
                "base": 43,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1421899977,
                "result'": 1012156867,
                "$cond'": true,
                "exponent'": 10,
                "base": 43,
                "exponent": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1012156867,
                "result'": 1012156867,
                "$cond'": true,
                "exponent'": 10,
                "base": 43,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1012156867,
                "result'": 573072321,
                "$cond'": true,
                "exponent'": 9,
                "base": 43,
                "exponent": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 573072321,
                "result'": 573072321,
                "$cond'": true,
                "exponent'": 9,
                "base": 43,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 573072321,
                "result'": -1127693973,
                "$cond'": true,
                "exponent'": 8,
                "base": 43,
                "exponent": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1127693973,
                "result'": -1127693973,
                "$cond'": true,
                "exponent'": 8,
                "base": 43,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1127693973,
                "result'": -1246200583,
                "$cond'": true,
                "exponent'": 7,
                "base": 43,
                "exponent": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1246200583,
                "result'": -1246200583,
                "$cond'": true,
                "exponent'": 7,
                "base": 43,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1246200583,
                "result'": -2047017517,
                "$cond'": true,
                "exponent'": 6,
                "base": 43,
                "exponent": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2047017517,
                "result'": -2047017517,
                "$cond'": true,
                "exponent'": 6,
                "base": 43,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2047017517,
                "result'": -2122407311,
                "$cond'": true,
                "exponent'": 5,
                "base": 43,
                "exponent": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -2122407311,
                "result'": -2122407311,
                "$cond'": true,
                "exponent'": 5,
                "base": 43,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -2122407311,
                "result'": -1069201157,
                "$cond'": true,
                "exponent'": 4,
                "base": 43,
                "exponent": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1069201157,
                "result'": -1069201157,
                "$cond'": true,
                "exponent'": 4,
                "base": 43,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1069201157,
                "result'": 1268990505,
                "$cond'": true,
                "exponent'": 3,
                "base": 43,
                "exponent": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1268990505,
                "result'": 1268990505,
                "$cond'": true,
                "exponent'": 3,
                "base": 43,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1268990505,
                "result'": -1267983133,
                "$cond'": true,
                "exponent'": 2,
                "base": 43,
                "exponent": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": -1267983133,
                "result'": -1267983133,
                "$cond'": true,
                "exponent'": 2,
                "base": 43,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": -1267983133,
                "result'": 1311300129,
                "$cond'": true,
                "exponent'": 1,
                "base": 43,
                "exponent": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 1311300129,
                "result'": 1311300129,
                "$cond'": true,
                "exponent'": 1,
                "base": 43,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 4,
            "mem": {
                "result": 1311300129,
                "result'": 551330699,
                "$cond'": true,
                "exponent'": 0,
                "base": 43,
                "exponent": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 2,
            "mem": {
                "result": 551330699,
                "result'": 551330699,
                "$cond'": false,
                "exponent'": 0,
                "base": 43,
                "exponent": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "find_power",
            "location": 3,
            "mem": {
                "result": 551330699,
                "result'": 551330699,
                "$cond'": false,
                "exponent'": 0,
                "$ret'": 551330699,
                "base": 43,
                "exponent": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

