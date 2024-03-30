# Test Report

Time: 2024-03-30 06:29:21.524422

### Base Program

```py
def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod
```

## Test Case 1

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[63]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[47]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[17]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[56]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 5

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[31]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 6

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[8]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 7

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[51]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 8

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[47]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 9

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[63]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 10

### Modified Program

```py

def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minNonZeroProduct\": {\"name\": \"minNonZeroProduct\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"mod\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"mod\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"value\": \"10\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"9\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"7\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"y\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"y\", {\"name\": \"Sub\", \"args\": [{\"name\": \"LShift\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"p\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"z\", \"val1\": {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"z\", {\"name\": \"pow\", \"args\": [{\"name\": \"y\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"z\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"mod\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minNonZeroProduct'\"}, \"types\": {\"mod\": \"*\", \"x\": \"*\", \"y\": \"*\", \"z\": \"*\"}}}}",
    "function": "minNonZeroProduct",
    "inputs": "[]",
    "args": "[64]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

