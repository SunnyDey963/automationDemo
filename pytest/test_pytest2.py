#fixtures
import pytest

def test_thirdinititalcheck(prerSetup):
    print('third test')

@pytest.mark.smoke
def test_fifthinititalcheck(prerSetup):
    print('fifth test')
