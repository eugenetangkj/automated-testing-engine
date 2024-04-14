# Test Report

Time: 2024-04-14 11:23:33.562907

### Base Program

```py
def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area
```

## Test Case 1

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[40, 17, 82, 2, 45, 8, 17, 10]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 17,
                "area1'": -630,
                "area2'": -56,
                "ax2": 82,
                "bx1": 45,
                "by2": 10,
                "$ret'": -686,
                "ax1": 40,
                "ay2": 2,
                "by1": 8,
                "overlap_width'": -28,
                "overlap_height'": -15,
                "bx2": 17
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 2

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[22, 68, 45, 79, 51, 78, 85, 53]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 68,
                "area1'": 253,
                "area2'": -850,
                "ax2": 45,
                "bx1": 51,
                "by2": 53,
                "$ret'": -597,
                "ax1": 22,
                "ay2": 79,
                "by1": 78,
                "overlap_width'": -6,
                "overlap_height'": -25,
                "bx2": 85
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 3

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[70, 39, 61, 50, 43, 11, 62, 78]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 39,
                "area1'": -99,
                "area2'": 1273,
                "ax2": 61,
                "bx1": 43,
                "by2": 78,
                "$ret'": 1174,
                "ax1": 70,
                "ay2": 50,
                "by1": 11,
                "overlap_width'": -9,
                "overlap_height'": 11,
                "bx2": 62
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 4

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[70, 97, 47, 45, 93, 58, 47, 35]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 97,
                "area1'": 1196,
                "area2'": 1058,
                "ax2": 47,
                "bx1": 93,
                "by2": 35,
                "$ret'": 2254,
                "ax1": 70,
                "ay2": 45,
                "by1": 58,
                "overlap_width'": -46,
                "overlap_height'": -62,
                "bx2": 47
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 5

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[24, 14, 97, 20, 75, 87, 39, 99]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 14,
                "area1'": 438,
                "area2'": -432,
                "ax2": 97,
                "bx1": 75,
                "by2": 99,
                "$ret'": 6,
                "ax1": 24,
                "ay2": 20,
                "by1": 87,
                "overlap_width'": -36,
                "overlap_height'": -67,
                "bx2": 39
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 6

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[96, 56, 33, 35, 98, 93, 45, 98]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 56,
                "area1'": 1323,
                "area2'": -265,
                "ax2": 33,
                "bx1": 98,
                "by2": 98,
                "$ret'": 1058,
                "ax1": 96,
                "ay2": 35,
                "by1": 93,
                "overlap_width'": -65,
                "overlap_height'": -58,
                "bx2": 45
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 7

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[66, 50, 59, 27, 74, 7, 61, 84]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 50,
                "area1'": 161,
                "area2'": -1001,
                "ax2": 59,
                "bx1": 74,
                "by2": 84,
                "$ret'": -840,
                "ax1": 66,
                "ay2": 27,
                "by1": 7,
                "overlap_width'": -15,
                "overlap_height'": -23,
                "bx2": 61
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 8

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[28, 82, 72, 92, 23, 69, 18, 3]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 82,
                "area1'": 440,
                "area2'": 330,
                "ax2": 72,
                "bx1": 23,
                "by2": 3,
                "$ret'": 770,
                "ax1": 28,
                "ay2": 92,
                "by1": 69,
                "overlap_width'": -10,
                "overlap_height'": -79,
                "bx2": 18
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 9

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[58, 12, 23, 34, 80, 16, 2, 96]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 12,
                "area1'": -770,
                "area2'": -6240,
                "ax2": 23,
                "bx1": 80,
                "by2": 96,
                "$ret'": -7010,
                "ax1": 58,
                "ay2": 34,
                "by1": 16,
                "overlap_width'": -78,
                "overlap_height'": 18,
                "bx2": 2
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 10

### Modified Program

```py

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"total_area\": {\"name\": \"total_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"ax1\", \"val1\": \"*\", \"valueArray\": [\"ax1\", \"*\"], \"valueList\": [\"ax1\", \"*\"]}, {\"val0\": \"ay1\", \"val1\": \"*\", \"valueArray\": [\"ay1\", \"*\"], \"valueList\": [\"ay1\", \"*\"]}, {\"val0\": \"ax2\", \"val1\": \"*\", \"valueArray\": [\"ax2\", \"*\"], \"valueList\": [\"ax2\", \"*\"]}, {\"val0\": \"ay2\", \"val1\": \"*\", \"valueArray\": [\"ay2\", \"*\"], \"valueList\": [\"ay2\", \"*\"]}, {\"val0\": \"bx1\", \"val1\": \"*\", \"valueArray\": [\"bx1\", \"*\"], \"valueList\": [\"bx1\", \"*\"]}, {\"val0\": \"by1\", \"val1\": \"*\", \"valueArray\": [\"by1\", \"*\"], \"valueList\": [\"by1\", \"*\"]}, {\"val0\": \"bx2\", \"val1\": \"*\", \"valueArray\": [\"bx2\", \"*\"], \"valueList\": [\"bx2\", \"*\"]}, {\"val0\": \"by2\", \"val1\": \"*\", \"valueArray\": [\"by2\", \"*\"], \"valueList\": [\"by2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"area1\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"area1\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ax1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ay1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"area2\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"area2\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"bx2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"by2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"overlap_width\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"overlap_width\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ax2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ax1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"bx1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"overlap_height\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"overlap_height\", {\"name\": \"Sub\", \"args\": [{\"name\": \"min\", \"args\": [{\"name\": \"ay2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by2\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"ay1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"by1\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}, {\"val0\": \"overlap_area\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"overlap_area\", {\"name\": \"Mult\", \"args\": [{\"name\": \"max\", \"args\": [{\"name\": \"overlap_width\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"max\", \"args\": [{\"name\": \"overlap_height\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"area1\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"area2\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"overlap_area\", \"primed\": true, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'total_area'\"}, \"types\": {\"overlap_area\": \"*\", \"area1\": \"*\", \"overlap_width\": \"*\", \"area2\": \"*\", \"overlap_height\": \"*\"}}}}",
    "function": "total_area",
    "inputs": "[]",
    "args": "[66, 37, 11, 65, 47, 53, 63, 12]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "total_area",
            "location": 1,
            "mem": {
                "overlap_area": "<undef>",
                "area1": "<undef>",
                "overlap_width": "<undef>",
                "area2": "<undef>",
                "overlap_height": "<undef>",
                "$ret": "<undef>",
                "overlap_area'": 0,
                "ay1": 37,
                "area1'": -1540,
                "area2'": -656,
                "ax2": 11,
                "bx1": 47,
                "by2": 12,
                "$ret'": -2196,
                "ax1": 66,
                "ay2": 65,
                "by1": 53,
                "overlap_width'": -55,
                "overlap_height'": -41,
                "bx2": 63
            },
            "isChecked": false
        }
    ]
}
```

</details>

