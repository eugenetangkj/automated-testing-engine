import os
from its_test_engine.enums import Language
from its_test_engine.its.test_result import (
    ItsTestSuite,
    ItsTestCase,
    ItsTestResult,
    ItsTestSuitesMarkdownWriter,
)


def test_its_test_suite_success():
    test_suite = ItsTestSuite(Language.PYTHON, "parser", "base_code")

    assert test_suite.language == Language.PYTHON
    assert test_suite.endpoint == "parser"
    assert not test_suite.test_cases

    test_case = ItsTestCase("modified_code")
    test_suite.add_test_case(test_case)

    test_result = ItsTestResult(True, "parser", "success")
    test_case.add_result(test_result)

    assert test_suite.is_success()
    assert test_case.is_success()


def test_its_test_suite_failure():
    test_suite = ItsTestSuite(Language.PYTHON, "parser", "base_code")

    assert test_suite.language == Language.PYTHON
    assert test_suite.endpoint == "parser"
    assert not test_suite.test_cases

    test_case = ItsTestCase("modified_code")
    test_suite.add_test_case(test_case)

    test_result = ItsTestResult(False, "parser", "failure")
    test_case.add_result(test_result)

    assert not test_suite.is_success()
    assert not test_case.is_success()


def test_its_markdown_writer():
    test_suite = ItsTestSuite(Language.PYTHON, "parser", "base_code")
    test_case = ItsTestCase("modified_code")
    test_result = ItsTestResult(True, "parser", "success")
    test_result2 = ItsTestResult(
        True,
        "parser",
        "success",
        '{"message": "this is a test"}',
        '{"message": "this is a test"}',
    )

    test_case.add_result(test_result)
    test_case.add_result(test_result2)
    test_suite.add_test_case(test_case)

    test_suite2 = ItsTestSuite(Language.PYTHON, "interpreter", "base_code")
    test_case2 = ItsTestCase("modified_code")
    test_result3 = ItsTestResult(True, "interpreter", "success")
    test_case2.add_result(test_result3)
    test_suite2.add_test_case(test_case2)

    writer = ItsTestSuitesMarkdownWriter("/tmp/test_results_single")
    writer.write(test_suite)

    assert os.path.exists("/tmp/test_results_single")
    assert os.listdir("/tmp/test_results_single")
    assert len(os.listdir("/tmp/test_results_single")) == 1

    # remove all files and directories
    for file in os.listdir("/tmp/test_results_single"):
        os.remove(os.path.join("/tmp/test_results_single", file))

    os.removedirs("/tmp/test_results_single")

    bulk_writer = ItsTestSuitesMarkdownWriter("/tmp/test_results_bulk")
    bulk_writer.bulk_write([test_suite, test_suite2])

    assert os.path.exists("/tmp/test_results_bulk")
    assert os.listdir("/tmp/test_results_bulk")
    assert len(os.listdir("/tmp/test_results_bulk")) == 2

    # remove all files and directories
    for file in os.listdir("/tmp/test_results_bulk"):
        os.remove(os.path.join("/tmp/test_results_bulk", file))

    os.removedirs("/tmp/test_results_bulk")
