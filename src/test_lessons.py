import pytest


@pytest.fixture()
def set_up():
    print("Set up")


def test_sending_mail_1(set_up):
    print("Test sending mail 1")


def test_sending_mail_2(set_up):
    print("Test sending mail 2")
