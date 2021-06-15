from typing import Type


class ConsoleInterface:

    def __init__(self) -> None:
        super().__init__()

    def ask_for_blik(self):
        return input("input blik code: ")

    def ask_for_card(self):
        return input("input card number: ").replace(" ", "")

    def inform_of_success(self, value):
        print("Payment of {} PLN was successful".format(int(value)))

    def inform_failure_blik(self):
        print("Failed to validate transaction with blik code.")

    def inform_failure_credit_card(self):
        print("Failed to validate transaction with credit card number.")

    def card_usage_info(self, card_number):
        print("Using card {}".format(card_number))

    def inform_of_failure(self):
        print("Failed to execute the transaction.")


