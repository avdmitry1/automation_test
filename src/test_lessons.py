import pytest



@pytest.fixture()
def set_up():
    print("Intro test")
    # yield is used to define generators. Here, it marks the end of
    # the setup code and the start of the teardown code. The teardown
    # code is run after the test has been run.
    yield
    print(" Outro test")


def test_sending_mail_1(set_up):
    print("Test sending mail 1")


def test_sending_mail_2(set_up):
    print("Test sending mail 2")
