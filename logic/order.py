from uuid import uuid4

from logic.menu_item import MenuItem


class Order:
    def __init__(self, items=[], id=uuid4()):
        self.items = items
        self.id = id

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item: MenuItem):
        self.items.remove(item)

    def get_total(self):
        return sum([x.price for x in self.items])
