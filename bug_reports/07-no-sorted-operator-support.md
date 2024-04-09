# Issue 7: No sorted operator support

## Description

The current version of the application does not support the sorted operator.

### Code

```py
def f():
    return sorted([3,2,1])
```

The code snippet above uses the `sorted` operator.

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"
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
  -d '{"language":"py","function":"f","inputs":"[]","args":"[]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"sorted\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"3\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"}'
```
