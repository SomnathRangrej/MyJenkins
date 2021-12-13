import pytest

@pytest.yield_fixture()
def setup():
    print("Once BEFORE every test method")
    yield                                 # yield keyword is important here, anything after yield will get executed after test run, anything before wil get executed before test run
    print("Once AFTER every test method")

def test_method1(setup):
    print("Test: test_method1")

def test_method2(setup):
    print("Test: test_method2")

def test_method3():
    print("Test: test_method3")

'''
Note:
    - You need NOT use yield_fixture() only in order to yield, you can use normal fixture also, it works fine
'''