import pytest

@pytest.fixture()
def setup():
    print("Once BEFORE every test method")

def test_method1(setup):
    print("Test: test_method1")

def test_method2(setup):
    print("Test: test_method2")

def test_method3():
    print("Test: test_method3")

'''
Note:
- The purpose of fixture is to provide fixed baseline, upon which test can reliably & repeatedly run
'''
