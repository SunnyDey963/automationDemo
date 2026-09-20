import pytest

@pytest.fixture(scope="function")
def prerSetup():
    print(" = prerSetup browser instance")