# Issue 6: No join operator support

## Description

The current version of the application does not support the join operator.

### Code

```py
def f():
    return ''.join(['a', 'b'])
```

The code snippet above uses the `join` operator. The interpreter does not support this feature.

```py
def f():
    return 'a' + 'b'
```

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"
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
  -d '{"language":"py","function":"f","inputs":"[]","args":"[]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"FuncCall\",\"args\":[{\"value\":\"join\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"name\":\"ListInit\",\"args\":[{\"value\":\"\\\"a\\\"\",\"line\":3,\"tokentype\":\"Constant\"},{\"value\":\"\\\"b\\\"\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"}'
```
