import uuid

from logic.console_interface import ConsoleInterface


class Payment:
    def __init__(self, name, interface=None):
        self.name = name
        self.console = interface or ConsoleInterface()

    def pay(self, value, id=uuid.uuid4()):
        self.id = id
        self.value = value

    def validate(self):
        return self.value >= 0


class Blik(Payment):
    def __init__(self, interface=None):
        super().__init__('blik')
        self.code = "not set"
        self.console = interface or ConsoleInterface

    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)
        self.code = self.console.ask_for_blik()

        if self.validate():
            self.console.inform_of_success(value)
        else:
            self.console.inform_failure_blik()

    def validate(self):
        if len(self.code) != 4:
            return False
        else:
            return True


class Card(Payment):
    def __init__(self, interface=None):
        super().__init__('card')
        self.card_number = "not set"
        self.console = interface or ConsoleInterface

    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)

        self.card_number = self.console.ask_for_card()
        self.console.card_usage_info(self.card_number)

        if self.validate():
            self.console.inform_of_success(value)
        else:
            self.console.inform_failure_credit_card()

    def validate(self):
        is_valid = len(self.card_number.replace(" ", "")) == 16

        if not is_valid:
            return is_valid

        return is_valid


class Cash(Payment):
    def __init__(self, interface=None):
        super().__init__('cash')
        self.console = interface or ConsoleInterface

    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)

        if self.validate():
            self.console.inform_of_success(value)
        else:
            self.console.inform_of_failure()

    def validate(self):
        return super().validate()
