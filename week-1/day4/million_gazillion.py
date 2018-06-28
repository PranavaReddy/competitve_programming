import unittest

class Trie(object):

    def __init__(self):
        self.root = {}

    def add_word(self, word):
        present_node = self.root
        new_word = False

        
        for char in word:
            if char not in present_node:
                new_word = True
                present_node[char] = {}
            present_node = present_node[char]
            
        if "i" not in present_node:
            new_word = True
            present_node["i"] = {}

        return new_word


class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)