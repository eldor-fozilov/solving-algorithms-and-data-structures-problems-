# O(n * m) time | O(n * m), n is the number of words in the input array and m is the 
# length of the longest word in the input array

def semordnilap(words):

    semordnilaps = []
    words_reverses = set()

    for word in words:
        reverse_word = word[::-1]
        if word in words_reverses:
            semordnilaps.append([word, reverse_word])
        else:
            words_reverses.add(reverse_word)
            
            
    return semordnilaps
