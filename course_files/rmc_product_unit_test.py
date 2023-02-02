import unittest
import sys
sys.path.append('data-collection-pipeline')

from example.product import Product
from example.cart import ShoppingCart

from hypothesis import given
import hypothesis.strategies as st

class ProductTestCase(unittest.TestCase):
    #@given(s=st.text())
    def test_generate_name(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'Shoes'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'Black'
        actual_value = small_black_shoes.transform_color_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        name = small_black_shoes.transform_name_for_sku()
        color = small_black_shoes.transform_color_for_sku()
        expected_value = "Shoes-S-Black"
        actual_value = f'{name}-{small_black_shoes.size}-{color}'
        self.assertEqual(expected_value, actual_value)


class CartTestCase(unittest.TestCase):
    def test_cart_initially_empty(self): 
        test_cart = ShoppingCart()
        #tests that, after creating the cart instance, it starts as an empty dictionary
        self.assertEqual(len(test_cart.products),0)

    def test_add_product(self): 
        #tests that, after adding a product to the cart, cart.products will be equal to a dictionary like this: {'SHOES-S-BLUE': {'quantity': 1}}
        test_cart = ShoppingCart()
        small_blue_shoes = Product('shoes', 'S', 'blue')
        test_cart.add_product(small_blue_shoes)
        test_dict = {'Shoes-S-Blue': {'quantity': 1}}
        self.assertEqual(test_cart.products, test_dict)

    def test_add_2_of_a_product(self):
        ## test that two of an item are added to the cart
        test_cart = ShoppingCart()
        small_blue_shoes = Product('shoes', 'S', 'blue')
        test_cart.add_product(small_blue_shoes, quantity=2)
        test_dict = {'Shoes-S-Blue': {'quantity': 2}}
        self.assertEqual(test_cart.products, test_dict)

    def test_add_2_different_products(self):
        ## test two different products are added to the cart
        test_cart = ShoppingCart()
        small_blue_shoes = Product('shoes', 'S', 'blue')
        large_red_shoes = Product('shoes', 'L', 'red')
        test_cart.add_product(small_blue_shoes, quantity=1)
        test_cart.add_product(large_red_shoes, quantity=1)
        test_dict = {'Shoes-S-Blue': {'quantity': 1}, 'Shoes-L-Red': {'quantity' : 1}}
        self.assertEqual(test_cart.products, test_dict)

    def test_remove_too_many(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')
        cart.add_product(product)
        cart.remove_product(product, quantity=2)

        self.assertDictEqual({}, cart.products)


unittest.main(argv=[''], verbosity=2, exit=False)