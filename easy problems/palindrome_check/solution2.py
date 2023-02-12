# Time Complexity: O(n), n is the number letters in the string
# Auxiliary Space Complexity: O(n)

def _isPalindrome(first, last, string):

    if first >= last:
        return True
    else:
        return string[first] == string[last] and _isPalindrome(first+1, last-1, string)


def isPalindrome(string):
    return _isPalindrome(0, len(string) - 1, string)