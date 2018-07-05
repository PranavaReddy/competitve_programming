import unittest
def get_closing_paren(sentence, start_index):
    braces=0
    position=start_index+1
    for position in range(start_index+1, len(sentence)):
        parenthesis=sentence[position]
        if parenthesis== '(':
            braces+= 1
        elif parenthesis == ')':
            if braces==0:
                return position
            else:
                braces-=1
    raise Exception("Invalid")

    



class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)