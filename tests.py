import pytest

@pytest.fixture()
def setup():
    print("Testing 1")

def method1(setup):
    print("Testing 2")

def method2(setup):
    print("Testing 3")