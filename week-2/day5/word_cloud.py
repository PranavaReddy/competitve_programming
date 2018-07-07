import unittest
import re

def word_cloud(input):
    special_characters=r"\.|!|\?"
    l1=re.split(special_characters,input)

    dic={}
    for i in l1:
        l2= re.split(r"[^a-zA-Z0-9-]+",i)
        for j in l2:
            c=dic.get(j,0)
            dic[j] =c+1

    def is_cap(j):
        l3=j[0:1]
        return l3 in j.upper()

    for a,l in a.items():
        if is_cap(a) and a.lower() in dic:
            c=a[a]
            dic[a.lower()]+=c
            del dic[a]

    return dic


class TestWordCloud(unittest.TestCase):
    def test_simple_sentence(self):
        input = 'I like cake'

       
        actual = word_cloud(input)

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        
        actual = word_cloud(input)
        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        
        actual = word_cloud(input)
        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

       
        actual = word_cloud(input)
        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        actual = word_cloud(input)

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)


    def test_examples(self):
        """test the given example"""
        test = 'After beating the eggs, Dana read the next step:' + \
            'Add milk and eggs, then add flour and sugar-free diet coke.'
        soln = {
            'After': 1,
            'Dana': 1,
            'add': 2,
            'and': 2,
            'beating': 1,
            'coke': 1,
            'diet': 1,
            'eggs': 2,
            'flour': 1,
            'milk': 1,
            'next': 1,
            'read': 1,
            'step': 1,
            'sugar-free': 1,
            'the': 2,
            'then': 1,
        }

        cloud = word_cloud(test)
        self.assertDictEqual(soln, cloud)

    def test_more_examples(self):
        "test some additional examples"

        tests = [
            ["We came, we saw, we conquered...then we ate Bill's "
             "(Mille-Feuille) cake."
             "The bill came to five dollars.",
             {
                 'Mille-Feuille': 1,
                 'The': 1,
                 'ate': 1,
                 'bill': 2,
                 'cake': 1,
                 'came': 2,
                 'conquered': 1,
                 'dollars': 1,
                 'five': 1,
                 's': 1,
                 'saw': 1,
                 'then': 1,
                 'to': 1,
                 'we': 4
             }
             ]
        ]

        for test, soln in tests:
            cloud = word_cloud(test)
            self.assertDictEqual(soln, cloud)



if __name__ == "__main__":
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWordCloud)
    unittest.TextTestRunner(verbosity=2).run(suite)
