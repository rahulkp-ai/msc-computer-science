def matrix_multiplication(A,B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Incompactable Dimensions")
    
    result = [ [0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    return result

A = [[1,2], [3,4]]
B = [[5,6], [7,8]]

print(matrix_multiplication(A,B))

def dot_product(A,B):
    rows_A = len(A)
    rows_B = len(B)

    if rows_A != rows_B:
        raise ValueError("Incompactable Dimensions")
    total = 0 
    for i in range(rows_A):
        total += A[i] * B[i]

    return total  
A = [2,-1,4]
B = [3,0,1]

print(dot_product(A,B))

def transpose(A):

    rows_A = len(A)
    cols_A = len(A[0])

    transposed = [[0 for _ in range(rows_A)] for _ in range(cols_A)]

    for i in range(rows_A):
        for j in range(cols_A):
            transposed[j][i] = A[i][j]

    return transposed

A = [[1,2,3],[4,5,6]]
print(transpose(A))

def determinant(A):
    rows_A = len(A)
    cols_A = len(A[0])

    if rows_A != 2 or cols_A != 2:
        raise ValueError("Incompactable Dimensions")

    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]

    det_A = (a*d) - (b*c)

    return det_A

A = [[2,3], [1,4]]

print(determinant(A))

import numpy as np
def orthogonal():
    vector1 = np.array([1,2,-1])
    vector2 = np.array([2,-1,0])

    dot_product = np.dot(vector1,vector2)

    print(dot_product)

    if dot_product == 0:
         print("The vectors are orthogonal.")
    else:
        print("The vectors are not orthogonal.")

orthogonal()