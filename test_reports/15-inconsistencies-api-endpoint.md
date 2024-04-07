# Issue 15: Inconsistencies with API Endpoints

## Description
We discovered a weird behaviour with the `error_localizer`, `feedback_error`, `feedback_fix` and `repair` endpoints. We have 2 different programs, let us call them Program A and Program B.

- When we pass Program A as both the base and modified programs to these endpoints, the endpoints return successfully.
- When we pass Program B as both the base and modified programs to these endpoints, the endpoints return successfully.
- When we pass Program A as the base program and Program B as the modified program, the endpoints return an error, with status code 500. This is not the intended behaviour, where we expected to see a comparison between Programs A and B instead.

#### Error Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/errorlocalizer. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```


### Inputs that worked with the error localizer

```py
# These sets of inputs work with the error localizer, using only Program A
base_program_string = "def main(x):\n\tx = x + 5\n\treturn x"
modified_program_string = "def main(x):\n\tx = x + 5\n\treturn x"
function_name = "main"
function_arguments = "[[66], [59], [64], [24], [85], [62], [68], [47], [92], [36]]"
```

```py
# These sets of inputs work with the error localizer, using only Program B
base_program_string = "def main(x):\n\tx = x + 5\n\tfor j in range(2, 5):\n\t\tx += 0\n\treturn x"
modified_program_string = "def main(x):\n\tx = x + 5\n\tfor j in range(2, 5):\n\t\tx += 0\n\treturn x"
function_name = "main"
function_arguments = "[[66], [59], [64], [24], [85], [62], [68], [47], [92], [36]]"
```


### Inputs that did not work with the error localizer
```py
# These sets of inputs do not work with the error localizer, where we used both
# Programs A and B
base_program_string = "def main(x):\n\tx = x + 5\n\treturn x"
modified_program_string = "def main(x):\n\tx = x + 5\n\tfor j in range(2, 5):\n\t\tx += 0\n\treturn x"
function_name = "main"
function_arguments = "[[66], [59], [64], [24], [85], [62], [68], [47], [92], [36]]"
```

### Error localizer input that did not work
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[66], [59], [64], [24], [85], [62], [68], [47], [92], [36]]"
}
```