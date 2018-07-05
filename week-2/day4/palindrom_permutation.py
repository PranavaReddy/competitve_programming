import unittest


def has_palindrome_permutation(the_string1):
    l=the_string1
    strs=['']*26
    count=0
    
    for i in range(0,len(l)):
    	
    	cal=ord(l[i])%97
    	if(strs[cal]==''):
    		strs[cal]=l[i]
    		count=count+1
    	else:
    		strs[cal]=''
    		count=count-1
    
    
    if(count==0 or count==1):
    	return True
    else:
    	return False

    
    

  


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string1(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string1(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
