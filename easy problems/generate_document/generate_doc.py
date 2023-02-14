# Time Complextiy: O(n+m), n is the number of characters in the "characters" string and
# m is the number of characters in the "document" string

# Space Complexity: O(c + l), c is the number of unique characters in the "characters" string and
# l is the number of unique characters in the "document" string

def generateDocument(characters, document):

    d_char_freq = {}
    d_doc_char_freq = {}

    for char in characters:
        if char in d_char_freq:
            d_char_freq[char] += 1
        else:
            d_char_freq[char] = 1

    for char in document:
        if char in d_doc_char_freq:
            d_doc_char_freq[char] += 1
        else:
            d_doc_char_freq[char] = 1

    for key in d_doc_char_freq.keys():
        if key not in d_char_freq:
            return False
        elif d_char_freq[key] < d_doc_char_freq[key]:
            return False

    return True