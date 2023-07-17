import pytest
from testcases.conftest import userservice_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return userservice_data.get(testcase_name)
