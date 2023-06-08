'''
Task Overview: Shopping Cart Total Price Calculation Unit Test

In this task, you will write unit tests for a function that calculates the total price of items in a shopping cart. The function takes a list of items, each represented by a dictionary with keys for 'name', 'price', and 'quantity'. Your objective is to ensure that the function produces the correct total price given different combinations of items.

Tasks:

    Understand the calculate_total_price function and its input requirements.
    Write test cases to cover different scenarios, including valid and invalid prices and quantities.
    Execute the unit tests and verify if the calculated total price matches the expected result.
    Analyze the test results and make any necessary adjustments to the function or test cases.
    Repeat steps 2-4 until you are confident in the accuracy and reliability of the calculate_total_price function.

By completing this task, you will gain experience in writing unit tests to validate the functionality of a real-world application. It will improve your ability to identify and handle different edge cases, ensuring the reliability of the code you test.
'''

def calculate_total_price(items):
    """Calculates the total price of items in the shopping cart.

    Args:
        items: A list of dictionaries. Each dictionary represents an item and has keys for 'name', 'price', and 'quantity'.

    Returns:
        The total price of all items in the shopping cart.
    """
    total_price = 0
    for item in items:
        total_price += item['price'] * item['quantity']
    return total_price


import unittest

class TestCalculateTotalPrice(unittest.TestCase):
    
    def test_single_item_single_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': 1}]
        self.assertEqual(calculate_total_price(items), 1.0)

    def test_single_item_multiple_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': 3}]
        self.assertEqual(calculate_total_price(items), 3.0)

    def test_multiple_items_single_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': 1},
                 {'name': 'Orange', 'price': 1.5, 'quantity': 1}]
        self.assertEqual(calculate_total_price(items), 2.5)

    def test_multiple_items_multiple_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': 2},
                 {'name': 'Orange', 'price': 1.5, 'quantity': 3}]
        self.assertEqual(calculate_total_price(items), 6.5)

    def test_zero_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': 0}]
        self.assertEqual(calculate_total_price(items), 0.0)

    def test_negative_quantity(self):
        items = [{'name': 'Apple', 'price': 1.0, 'quantity': -1}]
        with self.assertRaises(Exception):
            calculate_total_price(items)

    def test_negative_price(self):
        items = [{'name': 'Apple', 'price': -1.0, 'quantity': 1}]
        with self.assertRaises(Exception):
            calculate_total_price(items)

            
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateTotalPrice)

unittest.TextTestRunner().run(suite)

'''
OUTPUT:
..FF...
======================================================================
FAIL: test_negative_price (__main__.TestCalculateTotalPrice)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\migue\AppData\Local\Temp\ipykernel_22112\1197877496.py", line 33, in test_negative_price
    calculate_total_price(items)
AssertionError: Exception not raised

======================================================================
FAIL: test_negative_quantity (__main__.TestCalculateTotalPrice)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\migue\AppData\Local\Temp\ipykernel_22112\1197877496.py", line 28, in test_negative_quantity
    calculate_total_price(items)
AssertionError: Exception not raised

----------------------------------------------------------------------
Ran 7 tests in 0.005s

FAILED (failures=2)
'''

'''
This output is indicating that two of your tests have failed: test_negative_price and test_negative_quantity.

In both these test cases, you're expecting the function calculate_total_price to raise an Exception when the quantity or price is negative, which is a sensible expectation. This is signified by the with self.assertRaises(Exception): block in your test cases.

The error message "AssertionError: Exception not raised" means that an Exception was not raised when the calculate_total_price function was called with negative price or quantity. This suggests that your calculate_total_price function currently does not handle cases with negative price or quantity by raising an exception.

'''
'''
This script consists of a function named `calculate_total_price` and a collection of unit tests to ensure that `calculate_total_price` works as intended. 

The function `calculate_total_price` takes a list of items, where each item is represented as a dictionary with keys for 'name', 'price', and 'quantity'. The function then calculates the total cost of all items in the list by multiplying each item's price and quantity and adding these together.

The rest of the script is devoted to testing the `calculate_total_price` function with Python's built-in unittest framework. 

The `TestCalculateTotalPrice` class contains seven methods, each of which tests `calculate_total_price` under different conditions:

1. `test_single_item_single_quantity`: This test checks that the function correctly calculates the total cost when the list contains a single item with a quantity of 1.

2. `test_single_item_multiple_quantity`: This test checks that the function correctly calculates the total cost when the list contains a single item with a quantity greater than 1.

3. `test_multiple_items_single_quantity`: This test checks that the function correctly calculates the total cost when the list contains multiple items, each with a quantity of 1.

4. `test_multiple_items_multiple_quantity`: This test checks that the function correctly calculates the total cost when the list contains multiple items, each with a quantity greater than 1.

5. `test_zero_quantity`: This test checks that the function correctly handles a case where an item's quantity is 0. The expected total cost is 0 in this case.

6. `test_negative_quantity`: This test checks that the function raises an Exception when an item's quantity is negative, which is an invalid input.

7. `test_negative_price`: This test checks that the function raises an Exception when an item's price is negative, which is also an invalid input.

The final two lines create a test suite from the `TestCalculateTotalPrice` class and run the suite, which will execute all the tests. The results are displayed in the console, showing which tests passed or failed.
'''