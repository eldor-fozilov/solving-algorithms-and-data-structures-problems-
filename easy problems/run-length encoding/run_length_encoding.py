# Time Complexity: O(n), n is the length of the input string
# Space Complexity: O(n)

def runLengthEncoding(string):

    output = []
    str_len = len(string)

    i = 0
    while i < str_len:
        j = i
        count = 1
        while j < str_len - 1 and string[j] == string[j+1]:
            count += 1
            j += 1
        
        if count <= 9:
            output.append(str(count) + string[i])
        else:
            repeat = count // 9 # 9A9A9A...
            remainder = count % 9
            temp_str = [str(9) + string[i]] * repeat
            temp_str = ''.join(temp_str)
            temp_str += str(remainder) + string[i]
            output.append(temp_str)
        
        i = j + 1
    
    return ''.join(output)