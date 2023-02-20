# O(N) time | O(N) space - N is the total number of elements in the array

def spiralTraverse(array):
    
    output = []
    upper_left_row = 0
    bottom_left_row = len(array) - 1
    upper_left_col = 0
    upper_right_col = len(array[0]) - 1
    
    while upper_left_row <= bottom_left_row and upper_left_col <= upper_right_col:

        # top traversal
        for i in range(upper_left_col, upper_right_col + 1):
            output.append(array[upper_left_row][i])

        # right side traversal
        for i in range(upper_left_row + 1, bottom_left_row + 1):
            output.append(array[i][upper_right_col])
        
        # bottom traversal
        for i in range(upper_right_col - 1, upper_left_col - 1, -1):
            # edge case
            if upper_left_row == bottom_left_row:
                break
            output.append(array[bottom_left_row][i])

        # left side traversal
        for i in range(bottom_left_row - 1, upper_left_row, -1):
            # edge case
            if upper_left_col == upper_right_col:
                break
            output.append(array[i][upper_left_col])
            
        upper_left_row += 1
        bottom_left_row -= 1
        upper_right_col -= 1
        upper_left_col += 1

        
    return output
