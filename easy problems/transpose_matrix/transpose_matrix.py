# O(n*m) time | O(n*m) space - where n is the hight and m is the width of the matrix

def transposeMatrix(matrix):

    transpose_mat = [[] for i in range(len(matrix[0]))]
    for row in matrix:
        for index in range(len(row)):
            transpose_mat[index].append(row[index])            
    
    return transpose_mat
