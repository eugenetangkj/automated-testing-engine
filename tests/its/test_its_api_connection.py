import json
from unittest.mock import patch
import requests
import pytest
from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection

CODE = """
def add(a, b):
    return a + b
"""

# pylint: disable=line-too-long
PARSED_CODE = '{"importStatements":[],"fncs":{"add":{"name":"add","rettype":"*","initloc":1,"endloc":0,"params":[{"val0":"a","val1":"*","valueArray":["a","*"],"valueList":["a","*"]},{"val0":"b","val1":"*","valueArray":["b","*"],"valueList":["b","*"]}],"locexprs":{"1":[{"val0":"$ret","val1":{"name":"Add","args":[{"name":"a","primed":false,"line":3,"tokentype":"Variable"},{"name":"b","primed":false,"line":3,"tokentype":"Variable"}],"line":3,"tokentype":"Operation"},"valueArray":["$ret",{"name":"Add","args":[{"name":"a","primed":false,"line":3,"tokentype":"Variable"},{"name":"b","primed":false,"line":3,"tokentype":"Variable"}],"line":3}],"valueList":["$ret",{"name":"Add","args":[{"name":"a","primed":false,"line":3,"tokentype":"Variable"},{"name":"b","primed":false,"line":3,"tokentype":"Variable"}],"line":3}]}]},"loctrans":{"1":{}},"locdescs":{"1":"around the beginning of function \'add\'"},"types":{}}}}'
INTERPRETER_OUTPUT = '{"entries":[{"functionName":"add","location":1,"mem":{"a":1,"b":2,"$ret\'":3,"$ret":"<undef>"},"isChecked":false}]}'


def test_its_api_connection():
    language = Language.PYTHON
    its_api_connection = ItsApiConnection(language)

    parser_payload = its_api_connection.create_parser_request_payload(CODE)

    assert its_api_connection.call_parser_endpoint(parser_payload) == json.loads(
        PARSED_CODE
    )

    interpreter_payload = its_api_connection.create_interpreter_request_payload(
        json.loads(PARSED_CODE), "add", [], [1, 2]
    )

    interpreter_output = its_api_connection.call_interpreter_endpoint(
        interpreter_payload
    )

    assert interpreter_output == json.loads(INTERPRETER_OUTPUT)

    request_payload = its_api_connection.create_request_payload(
        parser_payload, parser_payload, "add", "[]", [[1, 2]]
    )

    assert its_api_connection.call_errorlocalizer_endpoint(request_payload) == {
        "errorLocations": {},
        "errorInputs": [],
    }

    assert its_api_connection.call_feedback_error_endpoint(request_payload) == []
    assert its_api_connection.call_feedback_fix_endpoint(request_payload) == []
    assert its_api_connection.call_repair_endpoint(request_payload) == [
        {"totalCost": 0, "localRepairs": []}
    ]


@patch("its_test_engine.its.its_api_connection.requests.post")
def test_its_api_connection_timeout(mocker):
    language = Language.PYTHON
    its_api_connection = ItsApiConnection(language)

    mocker.side_effect = requests.exceptions.Timeout()

    parser_payload = its_api_connection.create_parser_request_payload(CODE)

    with pytest.raises(Exception):
        its_api_connection.call_parser_endpoint(parser_payload)


@patch("its_test_engine.its.its_api_connection.requests.post")
def test_its_api_connection_error(mocker):
    language = Language.PYTHON
    its_api_connection = ItsApiConnection(language)

    mocker.return_value.status_code = 400
    mocker.return_value.text = "Bad request"

    parser_payload = its_api_connection.create_parser_request_payload(CODE)

    with pytest.raises(Exception):
        its_api_connection.call_parser_endpoint(parser_payload)
