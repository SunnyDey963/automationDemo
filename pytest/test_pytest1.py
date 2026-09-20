#fixtures
import pytest

import pytest
@pytest.fixture(scope="module")
def prerWork():
    print(" = setup browser instance")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print(" = setup browser instance - secondWork")
    yield #pause
    print("tear down validation")


@pytest.mark.skip
def test_inititalcheck(prerWork,secondWork):
    print('first test')
    assert prerWork == "pass"

def test_secondinititalcheck(prerSetup , secondWork):
    print('second test')


@pytest.mark.smoke
def test_fourthinititalcheck(prerSetup , secondWork):
    print('fourth test')
