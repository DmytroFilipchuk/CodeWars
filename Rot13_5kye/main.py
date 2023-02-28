import string
import unittest

def rot13(message):
    letters = string.ascii_lowercase * 2 + string.ascii_uppercase * 2
    output = ''

    for element in message:
        if element.isalpha():
            output += letters[letters.index(element) + 13]
        else:
            output += element

    return output

class tests(unittest.TestCase):
    def test_rot13_fixed_strings(self):
        self.assertEqual(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        self.assertEqual(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
                           'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')



if __name__ == "__main__":
    unittest.main()




