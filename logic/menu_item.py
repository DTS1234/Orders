import uuid

class MenuItem:
    def __init__(self, name, price, id=uuid.uuid4()):
        self.name = name
        self.price = price
        self.id = id