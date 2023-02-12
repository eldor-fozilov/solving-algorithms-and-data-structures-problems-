# Time Complexity: O(n), n is the number letters in the string
# Auxiliary Space Complexity: O(1)

def isPalindrome(string):
    
    str_len = len(string)
    for i in range(str_len):
        if string[i] != string[str_len - (i+1)]:
            return False
    return True
