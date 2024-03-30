# Issue 5: No proper while support in Interpreter

## Description

No proper while support in the interpreter.

### Code

```py
def f():
    while True:
        break
    return 0
```

```py
def f():
    i = 1
    while i:
        i -= 1
    return i
```

The code snippets above use `while` loop. The interpreter does not support this feature properly.

We notice that if the expression in the `while` loop is a binary operation, the interpreter will be able to evaluate the expression correctly.

```py
def f():
    i = 1
    while i < 0:
        i -= 1
    return i
```

### Input

```json
{
  "language": "py",
  "function": "f",
  "inputs": "[]",
  "args": "[]",
  "program_model": "{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"i\",\"val1\":{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},\"valueArray\":[\"i\",{\"value\":\"1\",\"line\":3}],\"valueList\":[\"i\",{\"value\":\"1\",\"line\":3}]}],\"2\":[{\"val0\":\"$cond\",\"val1\":{\"name\":\"i\",\"primed\":false,\"line\":4,\"tokentype\":\"Variable\"},\"valueArray\":[\"$cond\",{\"name\":\"i\",\"primed\":false,\"line\":4}],\"valueList\":[\"$cond\",{\"name\":\"i\",\"primed\":false,\"line\":4}]}],\"3\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"i\",\"primed\":false,\"line\":6,\"tokentype\":\"Variable\"},\"valueArray\":[\"$ret\",{\"name\":\"i\",\"primed\":false,\"line\":6}],\"valueList\":[\"$ret\",{\"name\":\"i\",\"primed\":false,\"line\":6}]}],\"4\":[{\"val0\":\"i\",\"val1\":{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5,\"tokentype\":\"Operation\"},\"valueArray\":[\"i\",{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5}],\"valueList\":[\"i\",{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5}]}]},\"loctrans\":{\"1\":{\"true\":2},\"2\":{\"false\":3,\"true\":4},\"3\":{},\"4\":{\"true\":2}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\",\"2\":\"the condition of the 'while' loop at line 4\",\"3\":\"*after* the 'while' loop starting at line 4\",\"4\":\"inside the body of the 'while' loop beginning at line 5\"},\"types\":{\"i\":\"*\"}}}}"
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
  -d '{"language":"py","function":"f","inputs":"[]","args":"[]","program_model":"{\"importStatements\":[],\"fncs\":{\"f\":{\"name\":\"f\",\"rettype\":\"*\",\"initloc\":1,\"endloc\":0,\"params\":[],\"locexprs\":{\"1\":[{\"val0\":\"i\",\"val1\":{\"value\":\"1\",\"line\":3,\"tokentype\":\"Constant\"},\"valueArray\":[\"i\",{\"value\":\"1\",\"line\":3}],\"valueList\":[\"i\",{\"value\":\"1\",\"line\":3}]}],\"2\":[{\"val0\":\"$cond\",\"val1\":{\"name\":\"i\",\"primed\":false,\"line\":4,\"tokentype\":\"Variable\"},\"valueArray\":[\"$cond\",{\"name\":\"i\",\"primed\":false,\"line\":4}],\"valueList\":[\"$cond\",{\"name\":\"i\",\"primed\":false,\"line\":4}]}],\"3\":[{\"val0\":\"$ret\",\"val1\":{\"name\":\"i\",\"primed\":false,\"line\":6,\"tokentype\":\"Variable\"},\"valueArray\":[\"$ret\",{\"name\":\"i\",\"primed\":false,\"line\":6}],\"valueList\":[\"$ret\",{\"name\":\"i\",\"primed\":false,\"line\":6}]}],\"4\":[{\"val0\":\"i\",\"val1\":{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5,\"tokentype\":\"Operation\"},\"valueArray\":[\"i\",{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5}],\"valueList\":[\"i\",{\"name\":\"Sub\",\"args\":[{\"name\":\"i\",\"primed\":false,\"line\":5,\"tokentype\":\"Variable\"},{\"value\":\"1\",\"line\":5,\"tokentype\":\"Constant\"}],\"line\":5}]}]},\"loctrans\":{\"1\":{\"true\":2},\"2\":{\"false\":3,\"true\":4},\"3\":{},\"4\":{\"true\":2}},\"locdescs\":{\"1\":\"around the beginning of function 'f'\",\"2\":\"the condition of the 'while' loop at line 4\",\"3\":\"*after* the 'while' loop starting at line 4\",\"4\":\"inside the body of the 'while' loop beginning at line 5\"},\"types\":{\"i\":\"*\"}}}}"}'
```

### Expected Output

It should return valid execution output. Answer is `0`
