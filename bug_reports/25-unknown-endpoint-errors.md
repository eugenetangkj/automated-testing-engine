# Issue 25: Unknown Endpoint Errors

## Description
In randomly generating programs, we found a program that led to a status code `500` error in the `feedback_error` and `feedback_fix` endpoints. However, what is weird is that this program leads to successful returns from the `errorlocalizer` and `repair` endpoints.


We used the **same** program for both the base and modified programs, and when we tested the program on Python IDE (Version `3.9`), the program is deemed to be valid.

### Base Program

```py
def func():
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

### Modified Program
```py
def func():
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

### Output

#### Error Localizer
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

#### Feedback Error
Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/feedback_error. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

Actual Output: None

#### Feedback Fix
Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/feedback_fix. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

#### Repair
```json
[
    {
        "totalCost": 0.0,
        "localRepairs": []
    }
]
```


## Related Test Reports
Refer to Test Report ID 8588b018.