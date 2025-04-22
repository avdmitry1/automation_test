import pytest


@pytest.mark.run(order=2)
def test_method_1(set_up):
    print("Test method 1")


@pytest.mark.run(order=1)
def test_method_2(set_up):
    print("Test method 2")


@pytest.mark.run(order=4)
def test_method_3(set_up):
    print("Test method 3")


@pytest.mark.run(order=3)
def test_method_4(set_up):
    print("Test method 4")


@pytest.mark.run(order=5)
def test_method_5(set_up):
    print("Test method 5")
