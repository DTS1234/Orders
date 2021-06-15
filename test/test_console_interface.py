from unittest import TestCase
from unittest.mock import patch

import mock as mock

from logic.console_interface import ConsoleInterface


class TestConsoleInterface(TestCase):

    def test_ask_for_blik(self):
        subject = ConsoleInterface()
        with mock.patch('builtins.input', return_value="1111"):
            self.assertEqual("1111", subject.ask_for_card())

    def test_ask_for_card(self):
        subject = ConsoleInterface()
        with mock.patch('builtins.input', return_value="1111 1111 1111 1111"):
            self.assertEqual("1111111111111111", subject.ask_for_card())

    @patch('builtins.print')
    def test_inform_of_card_usage(self, mock_print):
        subject = ConsoleInterface()
        subject.card_usage_info("1111 1111 1111 1111")
        mock_print.assert_called_with('Using card 1111 1111 1111 1111')

    @patch('builtins.print')
    def test_inform_of_success(self, mock_print):
        subject = ConsoleInterface()
        subject.inform_of_success(100)
        mock_print.assert_called_with('Payment of 100 PLN was successful')

    @patch('builtins.print')
    def test_inform_of_failure_blik(self, mock_print):
        subject = ConsoleInterface()
        subject.inform_failure_blik()
        mock_print.assert_called_with('Failed to validate transaction with blik code.')

    @patch('builtins.print')
    def test_inform_failure_credit_card(self, mock_print):
        subject = ConsoleInterface()
        subject.inform_failure_credit_card()
        mock_print.assert_called_with('Failed to validate transaction with credit card number.')

    @patch('builtins.print')
    def test_inform_failure(self, mock_print):
        subject = ConsoleInterface()
        subject.inform_of_failure()
        mock_print.assert_called_with("Failed to execute the transaction.")