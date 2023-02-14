# O(n) time | O(1) space - where n is the length of the input string. The constant space is because the input
# string only has lowercase English-alphabet letters; thus the dictioonary will never have more than 
# 26 character frequencies.

def firstNonRepeatingCharacter(string):

    d = {}
    for index, letter in enumerate(string):
        d[letter] = d.get(letter, 0) + 1
    
    for i in range(len(string)):
        letter = string[i]
        if d[letter] == 1:
            return i
    
    return -1
