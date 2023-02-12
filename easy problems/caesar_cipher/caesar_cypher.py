# Time Complexity: O(n), n is the number of letters in the string
# Space Complexity: O(n)

def caesarCipherEncryptor(string, key):

    encypted_message = []
    for letter in string:
        new_order =  ord(letter) + key % 26
        encypted_letter = chr(new_order if new_order <= 122 else 96 + new_order % 122)
        encypted_message.append(encypted_letter) 

    return "".join(encypted_message)
    