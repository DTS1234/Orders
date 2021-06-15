import uuid

class Payment:
    def __init__(self, name):
        self.name = name

    def pay(self, value, id=uuid.uuid4()):
        self.id = id
        self.value = value

class Blik(Payment):
    def __init__(self):
        super().__init__('blik')
    
    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)
        code = int(input("input blik code: "))
        print("Payment of {} PLN was succesful".format(value))

class Card(Payment):
    def __init__(self):
        super().__init__('card')

    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)
        number_str = input("input card number: ").replace(" ", "")
        number = int(number_str)
        print("Using card {}".format(number))
        print("Payment of {} PLN was succesful".format(value))

class Cash(Payment):
    def __init__(self):
        super().__init__('cash')

    def pay(self, value, id=uuid.uuid4()):
        super().pay(value, id)
        print("Payment of {} PLN was succesful".format(value))
