from unittest import TestCase
from unittest.mock import Mock
from uuid import uuid4

from logic.console_interface import ConsoleInterface
from logic.payment import Cash


class TestCash(TestCase):

    def test_cashPaymentValid(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        subject = Cash(console_interface_spy)
        # when
        subject.pay(1200, uuid4())
        # then
        console_interface_spy.inform_of_success.assert_called_with(1200)

    def test_cashPaymentInValidCode(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        subject = Cash(console_interface_spy)
        # when
        subject.pay(-1, uuid4()) # wrong value
        # then
        console_interface_spy.inform_of_failure.assert_called_with()

    def test_cashValidateWrongValue(self):
        # given
        subject = Cash()
        subject.value = -1
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, False)

    def test_cardValidateValidValue(self):
        # given
        subject = Cash()
        subject.value = 100
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, True)
