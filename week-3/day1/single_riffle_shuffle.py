import unittest
def is_single_riffle(half1, half2, shuffled_deck):
    i=0
    j=0
    shuffled_deck=shuffled_deck
    while(i<len(half1) and j<len(half2)):
    	if(half1[i]<half2[j]):
    		if(shuffled_deck[i+j]!=half1[i]):
    			return False
            i=i+1
    	else:
    		if(shuffled_deck[i+j]!=half2[j]):
    			return False
    		j=j+1
    while(i<len(half1)):
    	if(shuffled_deck[i+j]!=half1[i]):
    		return False
    
    	i=i+1
    
    while(j<len(half2)):
    	if(shuffled_deck[i+j]!=half2[j]):
    		return False
    	
    	j=j+1
    
    
    if(len(half1)+len(half2)<len(shuffled_deck)):
        return False
    return True



class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
