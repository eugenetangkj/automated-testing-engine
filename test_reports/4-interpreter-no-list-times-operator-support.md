# Issue 4: No list times operator support in Interpreter

## Description

No list times operator support in the interpreter.

### Code

```py
def f():
    dp = [0] * 2
    return dp[0]
```

The code snippet above uses `*` operator to create a list with a specified length. The interpreter does not support this feature.

However, it works with the following code snippet:

```py
def f():
    dp = [0, 0]
    return dp[0]
```

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"dp\",\"val1\":{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"dp\",{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3}],\"valueList\":[\"dp\",{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{\"dp\":\"*\"}}}}"
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
  -d '{"language":"py","function":"f","inputs":"[]","args":"[]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"dp\",\"val1\":{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"dp\",{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3}],\"valueList\":[\"dp\",{\"name\":\"Mult\",\"args\":[{\"name\":\"ListInit\",\"args\":[{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3,\"tokentype\":\"Operation\"},{\"value\":\"2\",\"line\":3,\"tokentype\":\"Constant\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{\"dp\":\"*\"}}}}"}'
```

### Expected Output

It should return valid execution output.
