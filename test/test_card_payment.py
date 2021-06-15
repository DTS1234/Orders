from unittest import TestCase
from unittest.mock import Mock
from uuid import uuid4

from logic.console_interface import ConsoleInterface
from logic.payment import Card


class TestCard(TestCase):


    def test_cardPaymentValid(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        console_interface_spy.ask_for_card.return_value = '1010 1023 1312 1234'
        subject = Card(console_interface_spy)
        # when
        subject.pay(100, uuid4())
        # then
        console_interface_spy.inform_of_success.assert_called_with(100)
        console_interface_spy.card_usage_info.assert_called_with('1010 1023 1312 1234')

    def test_cardPaymentInValid(self):
        # given
        console_interface_spy = Mock(ConsoleInterface)
        console_interface_spy.ask_for_card.return_value = '1010 1023 1312 124'
        subject = Card(console_interface_spy)
        # when
        subject.pay(100, uuid4())
        # then
        console_interface_spy.inform_failure_credit_card(100)

    def test_cardValidateTooLong(self):
        # given
        subject = Card()
        subject.card_number = '1010 1023 1312 124324'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, False)

    def test_cardValidateValid(self):
        # given
        subject = Card()
        subject.card_number = '1010 1023 1312 1241'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, True)

    def test_cardValidateTooShort(self):
        # given
        subject = Card()
        subject.card_number = '1010 1023 1312 124'
        # when
        actual = subject.validate()
        # then
        self.assertEqual(actual, False)