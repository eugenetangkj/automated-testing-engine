# Issue 8: No reversed operator support

## Description

The current version of the application does not support the reversed operator.

### Code

```py
def f():
    return reversed([3,2,1])
```

The code snippet above uses the `reversed` operator.

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"
}
```

### Output

```json
null
```

### Steps to Reproduce

```bash
curl -X 'POST' 'https://its.comp.nus.edu.sg/cs3213/interpreter' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"language":"py","function":"f","inputs":"[]","args":"[]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"reversed\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"}'
```
