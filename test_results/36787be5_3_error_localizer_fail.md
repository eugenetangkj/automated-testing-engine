# Test Report

Time: 2024-04-07 15:52:31.071726

### Base Program

```py
def main(g, h):
	diff = g - h
	return diff
```

## Test Case 1

### Modified Program

```py
def main(g, h):
	g, h = h, g
	diff = h - g
	return diff
```

<details>
<summary>error_localizer endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"h\", \"val1\": {\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"h\", {\"name\": \"g\", \"primed\": false, \"line\": 2}], \"valueList\": [\"h\", {\"name\": \"g\", \"primed\": false, \"line\": 2}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"h\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"g\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"h\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"g\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"h\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"g\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"h\": \"*\", \"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[48, 58], [14, 1], [39, 97], [75, 65], [35, 92], [26, 68], [79, 37], [63, 13], [57, 40], [100, 32]]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/errorlocalizer. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

Actual Output: None

</details>

