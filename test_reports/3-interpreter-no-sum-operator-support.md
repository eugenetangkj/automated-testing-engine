# Issue 3: No sum operator support in Interpreter

## Description

No sum operator support in the interpreter.

### Code

```py
def f(nums):
    return sum(nums)
```

The code snippet above uses `sum` operator to calculate the sum of elements in the list. The interpreter does not support this feature.

However, it works with the following code snippet:

```py
def f(nums):
    total = 0
    for num in nums:
        total += num
    return total
```

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[[100, 100, 2]]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[{\"val0\":\"nums\",\"val1\":\"*\",\"valueArray\":[\"nums\",\"*\"],\"valueList\":[\"nums\",\"*\"]}],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"
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
  -d '{"language":"py","function":"f","inputs":"[]","args":"[[100, 100, 2]]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[{\"val0\":\"nums\",\"val1\":\"*\",\"valueArray\":[\"nums\",\"*\"],\"valueList\":[\"nums\",\"*\"]}],\"locexprs\":{\"1\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3,\"tokentype\":\"Operation\"},\"valueArray\":[\"$ret\",{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3}],\"valueList\":[\"$ret\",{\"name\":\"sum\",\"args\":[{\"name\":\"nums\",\"primed\":false,\"line\":3,\"tokentype\":\"Variable\"}],\"line\":3}]}]},\"loctrans\":{\"1\":{}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\"},\"types\":{}}}}"}'
```

### Expected Output

It should return valid execution output.
