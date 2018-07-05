import unittest


def get_permutations(string):
    l=0
    set1=set()
    length=len(string)-1
    if(len(string)==0):
        set1.add(string)
        return set1
    permute(list(string),l,length,set1)
    return set1
    
def toString(List):
    return ''.join(List)
     
    
def permute(array, l,length,set1):
    if l==length:
        k=toString(array)
        set1.add(k)
        print(set1)
    else:
        for i in range(l,length+1):
            temp=array[l]
            array[l]=array[i]
            array[i]=temp
            permute(array, l+1, length,set1)
            
            array[l],array[i] = array[i], array[l] 
    

    return set1


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
