import unittest
def is_valid(code):
    stack1 = []
    for brace in code:
        if brace == ')':
            if len(stack1)==0 or stack1.pop()!='(':
                return False
        elif brace == '}':
            if len(stack1)==0 or stack1.pop()!='{':
                return False
        elif brace == ']':
            if len(stack1)==0 or stack1.pop()!='[':
                return False
        elif brace == '(' or brace == '{' or brace == '[':
            stack1.append(brace)
    return len(stack1)==0

  








class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)