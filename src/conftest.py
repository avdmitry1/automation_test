import pytest


@pytest.fixture()
def set_up():
    print("Intro test")
    yield
    print(" Outro test")


@pytest.fixture(scope="function")
def set_up_module():
    print("Starting test")
    yield
    print(" Ending test")
