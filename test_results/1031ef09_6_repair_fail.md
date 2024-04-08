# Test Report

Time: 2024-04-08 07:09:57.043522

### Base Program

```py
def main():
	my_list = []
	if not my_list:
		return 1
	else:
		return 0
```

## Test Case 1

### Modified Program

```py
def main():
	my_list = []
	if not my_list:
		return 1
	else:
		return 0
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"my_list\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"my_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/repair. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: java.lang.NullPointerException\n\nError: java.lang.ClassCastException: class java.util.ArrayList cannot be cast to class java.lang.Boolean (java.util.ArrayList and java.lang.Boolean are in module java.base of loader 'bootstrap')\n\tat sg.edu.nus.se.its.interpreter.operations.ExecuteOperationUtils.evaluateToBoolean(ExecuteOperationUtils.java:82)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.NotOperation.executeUnaryOperation(NotOperation.java:21)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.NotOperation.executeUnaryOperation(NotOperation.java:8)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.UnaryOperation.executeFixParameterOperation(UnaryOperation.java:75)\n\tat sg.edu.nus.se.its.interpreter.operations.FixParameterOperationContext.executeFixParameterOperation(FixParameterOperationContext.java:26)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFixParamOp(PyInterpreter.java:527)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeOperation(PyInterpreter.java:415)\n\tat sg.edu.nus.se.its.model.Operation.execute(Operation.java:60)\n\tat sg.edu.nus.se.its.interpreter.operations.other.IteOperation.getParamFromMemory(IteOperation.java:47)\n\tat sg.edu.nus.se.its.interpreter.operations.other.IteOperation.executeIteOperation(IteOperation.java:38)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFixParamOp(PyInterpreter.java:464)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeOperation(PyInterpreter.java:415)\n\tat sg.edu.nus.se.its.model.Operation.execute(Operation.java:60)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.execute(PyInterpreter.java:144)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeStatement(PyInterpreter.java:592)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeBlock(PyInterpreter.java:554)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.getTraceFromFunctionExecution(PyInterpreter.java:171)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFunction(PyInterpreter.java:154)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.lambda$executeProgram$0(PyInterpreter.java:78)\n\tat java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)\n\tat java.base/java.lang.Thread.run(Thread.java:829)\njava.lang.ClassCastException: class java.util.ArrayList cannot be cast to class java.lang.Boolean (java.util.ArrayList and java.lang.Boolean are in module java.base of loader 'bootstrap')\n\tat sg.edu.nus.se.its.interpreter.operations.ExecuteOperationUtils.evaluateToBoolean(ExecuteOperationUtils.java:82)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.NotOperation.executeUnaryOperation(NotOperation.java:21)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.NotOperation.executeUnaryOperation(NotOperation.java:8)\n\tat sg.edu.nus.se.its.interpreter.operations.unary.UnaryOperation.executeFixParameterOperation(UnaryOperation.java:75)\n\tat sg.edu.nus.se.its.interpreter.operations.FixParameterOperationContext.executeFixParameterOperation(FixParameterOperationContext.java:26)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFixParamOp(PyInterpreter.java:527)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeOperation(PyInterpreter.java:415)\n\tat sg.edu.nus.se.its.model.Operation.execute(Operation.java:60)\n\tat sg.edu.nus.se.its.interpreter.operations.other.IteOperation.getParamFromMemory(IteOperation.java:47)\n\tat sg.edu.nus.se.its.interpreter.operations.other.IteOperation.executeIteOperation(IteOperation.java:38)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFixParamOp(PyInterpreter.java:464)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeOperation(PyInterpreter.java:415)\n\tat sg.edu.nus.se.its.model.Operation.execute(Operation.java:60)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.execute(PyInterpreter.java:144)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeStatement(PyInterpreter.java:592)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeBlock(PyInterpreter.java:554)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.getTraceFromFunctionExecution(PyInterpreter.java:171)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.executeFunction(PyInterpreter.java:154)\n\tat sg.edu.nus.se.its.interpreter.PyInterpreter.lambda$executeProgram$0(PyInterpreter.java:78)\n\tat java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)\n\tat java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)\n\tat java.base/java.lang.Thread.run(Thread.java:829)\njava.lang.NullPointerException\n\tat sg.edu.nus.se.its.errorlocalizer.BasicErrorLocalizer.matchTraceLocations(BasicErrorLocalizer.java:80)\n\tat sg.edu.nus.se.its.errorlocalizer.BasicErrorLocalizer.localizeErrors(BasicErrorLocalizer.java:137)\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:169)\nException in thread \"main\" java.lang.RuntimeException: java.lang.NullPointerException\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:189)\nCaused by: java.lang.NullPointerException\n\tat sg.edu.nus.se.its.errorlocalizer.BasicErrorLocalizer.matchTraceLocations(BasicErrorLocalizer.java:80)\n\tat sg.edu.nus.se.its.errorlocalizer.BasicErrorLocalizer.localizeErrors(BasicErrorLocalizer.java:137)\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:169)\n"}
```

Actual Output: None

</details>

