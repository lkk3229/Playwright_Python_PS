#Fixtures
import pytest


@pytest.fixture(scope="module")         # if scope = "function" then it will run before every test  # if scope = "Module" then it will run once only in this whole page.
def preWork():
    print("preWork")
    return "fail"

@pytest.fixture(scope="function")         # if scope = "function" then it will run before every test  # if scope = "Module" then it will run once only in this whole page.
def SecondpreWork():
    print("SecondpreWork")
    yield    #pause
    print("tear down SecondpreWork")

def test_initialcheck(preWork, SecondpreWork):
    print("initialcheck")
    assert preWork == "fail"

def test_test(preSetWork, SecondpreWork):
    print("test")
