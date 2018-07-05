import unittest
def  max_duffel_bag_val(cake_tuples,weight_capacity):

    while (0,0) in cake_tuples:
        cake_tuples.pop(cake_tuples.index((0,0)))

    try:

        for cake in cake_tuples:
            cake[1]/cake[0]

    except ZeroDivisionError:
        return float('/////')
    
   
    dic = {} 
    for i in range(0,weight_capacity+1):

       maximum_val = 0
        for cake in cake_tuples:
            temp = i - cake[0]

            if temp >= 0: 
                val = cake[1] + dic[temp]

                if val > maximum_val:
                   maximum_val = val 
        dic[i] =maximum_val 
    return maximum_val



class Test(unittest.TestCase): 

    def test_one_cake(self):
        actual = max_duffel_bag_val([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_val([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_val([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_val([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_val_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_val([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_weight_capacity(self):
        actual = max_duffel_bag_val([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_val_and_weight(self):
        actual = max_duffel_bag_val([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_val_and_zero_weight(self):
        actual = max_duffel_bag_val([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)