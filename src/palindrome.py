'''
Created on 11.12.2011

@author: Pavel Vavruska
'''
from math import floor


def is_anagram_of_palindrome(str):

    # Getting count of every single character in the string
    dic_char = {}
    for character in str:
        if character in dic_char:
            dic_char[character] += 1
        else:
            dic_char[character] = 1

    # Getting the counts of odd character count
    odd_count = 0
    for count in dic_char:
        if dic_char.get(count) % 2 != 0:
            odd_count += 1
            
    # There can be only one (or none) odd character count
    if odd_count > 1:
        return False
    else:
        return True

def is_palindrome(str):

    halfOfInput = int(floor(len(str) / 2))
    str_reversed = str[::-1]

    if str[ : halfOfInput] == str_reversed[ : halfOfInput]:
        result = True
    else:
        result = False
    return result

def main():

    print """
    #===========================================================================
    # Is the word an anagram of palindrome?                 Pavel Vavruska 2011
    #===========================================================================
    """

    test_string = raw_input("Enter a string:") # nolemonnomelon
    
    print '\nIs the word "%s" an anagram of palindrome? %10s!' %(test_string.upper(),
                                is_anagram_of_palindrome(test_string.lower()))

    print 'Is the word "%s" a palindrome? %22s!' %(test_string.upper(),
                                is_palindrome(test_string.lower()))

if __name__ == '__main__':
    main()