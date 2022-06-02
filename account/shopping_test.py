import shopping
import unittest

class ShoppingTest(unittest.TestCase):
    def test_that_shopping_class_can_be_created(self):
        my_shopping = shopping.Shopping("flo_mama",[])
        self.assertIsNotNone(my_shopping)
        self.assertIsInstance(my_shopping,shopping.Shopping)

    def test_that_items_can_be_added_to_shopping_chart(self):
        my_shopping = shopping.Shopping("flo_mama",[])
        my_shopping.add("grace")
        self.assertEqual("grace", my_shopping.item(0))

    def test_shopping_has_length(self):
        my_shopping = shopping.Shopping("flo_mama",[])
        self.assertTrue(3,my_shopping.length)
    # def test_





