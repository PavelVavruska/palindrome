'''
Created on 11.12.2011

@author: Pavel Vavruska
'''
import unittest

from src.palindrome import is_anagram_of_palindrome
from src.palindrome import is_palindrome


class Test(unittest.TestCase):

    def test_anagram_of_palindrome(self):
        test_string = 'asaf' # is NOT an anagram of palindrome

        self.assertEqual(is_anagram_of_palindrome(test_string), False,
                 "Word %s is not anagram of palindrome!" %(test_string))

        test_string = 'nolemonnomelon' # is an anagram of palindrome

        self.assertEqual(is_anagram_of_palindrome(test_string), True,
                 "Word %s is anagram of palindrome!" %(test_string))
        
        test_string = 'nolemonnomelno' # is an anagram of palindrome

        self.assertEqual(is_anagram_of_palindrome(test_string), True,
                 "Word %s is anagram of palindrome!" %(test_string))
        
    def test_palindrome(self):
        test_string = 'asaf' # is NOT a palindrome

        self.assertEqual(is_palindrome(test_string), False,
                 "Word %s is not palindrome!" %(test_string))

        test_string = 'nolemonnomelon' # is apalindrome

        self.assertEqual(is_palindrome(test_string), True,
                 "Word %s is palindrome!" %(test_string))
       
        test_string = 'nolemonnomelno' # is NOT a palindrome

        self.assertEqual(is_palindrome(test_string), False,
                 "Word %s is not palindrome!" %(test_string))

if __name__ == "__main__":
    unittest.main()