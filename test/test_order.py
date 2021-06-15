from unittest import TestCase
from uuid import uuid4

from logic.menu_item import MenuItem
from logic.order import Order


class TestOrder(TestCase):

    def setUp(self) -> None:
        self.test_orders = []
        self.subject = Order(self.test_orders, uuid4())
        super().setUp()

    def test_shouldAddOneItem(self):
        # given
        item = MenuItem("item 1", 12.00, uuid4())
        # when
        self.subject.add_item(item)
        # then
        self.assertEqual(self.subject.items[0], item)

    def test_shouldAddThreeItems(self):
        # given
        item1 = MenuItem("item 1", 12.00, uuid4())
        item2 = MenuItem("item 2", 11.00, uuid4())
        item3 = MenuItem("item 3", 15.00, uuid4())
        # when
        self.subject.add_item(item1)
        self.subject.add_item(item2)
        self.subject.add_item(item3)
        # then
        self.assertEqual(self.subject.items[2], item3)
        self.assertEqual(self.subject.items[1], item2)
        self.assertEqual(self.subject.items[0], item1)

    def test_shouldRemoveOneItem(self):
        # given
        item1 = MenuItem("item 1", 12.00, uuid4())
        item2 = MenuItem("item 2", 11.00, uuid4())
        item3 = MenuItem("item 3", 15.00, uuid4())
        self.subject.items = [item1, item2, item3]
        # when
        self.subject.remove_item(item3)
        # then
        self.assertEqual(self.subject.items[0], item1)
        self.assertEqual(self.subject.items[1], item2)

    def test_shouldRemoveAllItem(self):
        # given
        item1 = MenuItem("item 1", 12.00, uuid4())
        item2 = MenuItem("item 2", 11.00, uuid4())
        item3 = MenuItem("item 3", 15.00, uuid4())
        self.subject.items = [item1, item2, item3]
        # when
        self.subject.remove_item(item3)
        self.subject.remove_item(item2)
        self.subject.remove_item(item1)
        # then
        self.assertEqual(len(self.subject.items), 0)

    def test_shouldReturnSumOfPrices(self):
        # given
        item1 = MenuItem("item 1", 12.00, uuid4())
        item2 = MenuItem("item 2", 11.00, uuid4())
        item3 = MenuItem("item 3", 15.00, uuid4())
        self.subject.items = [item1, item2, item3]
        # when
        actual = self.subject.get_total()
        # then
        self.assertEqual(actual, 38.00)
