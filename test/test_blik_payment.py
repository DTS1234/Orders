from unittest import TestCase
from unittest.mock import Mock
from uuid import uuid4

from logic.console_interface import ConsoleInterface
from logic.payment import Blik


class TestBlikPayment(TestCase):

    def test_blikPaymentValidCode(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        console_interface_spy.ask_for_blik.return_value = '1010'  # stubbing valid code
        subject = Blik(console_interface_spy)
        # when
        subject.pay(10, uuid4())
        # then
        console_interface_spy.inform_of_success.assert_called_with(
            10)  # verifying if console success information was invoked

    def test_blikPaymentInValidCode(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        console_interface_spy.ask_for_blik.return_value = '110'  # stubbing invalid code
        subject = Blik(console_interface_spy)
        # when
        subject.pay(10, uuid4())
        # then
        console_interface_spy.inform_failure_blik.assert_called_with()  # verifying if failure information was invoked

    def test_blikValidateTooLongCode(self):
        # given
        subject = Blik()
        subject.code = '12345'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, False)

    def test_blik_validate_valid(self):
        # given
        subject = Blik()
        subject.code = '1234'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, True)

    def test_blik_validate_too_short(self):
        # given
        subject = Blik()
        subject.code = '124'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, False)
