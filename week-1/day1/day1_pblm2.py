import unittest
def apple_Stock(stock_values):
    l = len(stock_values)
    if l < 2:
        raise Exception
    else:
        least_profit = stock_values[0]
        final_profit = stock_values[1]-stock_values[0]
        for i in range(1,k):
            pre_cost = stock_values[i]
            profit = pre_cost - least_profit
            final_profit = max(final_profit,profit)
            least_profit = min(least_profit,pre_cost)
    return final_profit



class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = apple_Stock([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = apple_Stock([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = apple_Stock([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = apple_Stock([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = apple_Stock([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            apple_Stock([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            apple_Stock([])

unittest.main(verbosity=2)
    
applestock.py
Displaying applestock.py.