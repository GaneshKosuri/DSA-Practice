# --EASY--
# https://leetcode.com/problems/matrix-diagonal-sum/description/

# Solution starts
def diagonalSum(mat):
    sum = 0
    matrix_length = len(mat)
    for i in range(matrix_length):
        sum += mat[i][i]
        sum += mat[matrix_length-i-1][i]
    if(matrix_length%2):
        index = matrix_length//2
        sum -= mat[index][index]
    return sum
# Solution ends

# Demo purpose
size = int(input("Enter n x n matrix size: "))
matrix = []
for i in range(size):
    matrix.append(list(map(int,input("Enter the numbers separated by space for row {} : ".format((i+1))).strip().split()))[:size])
print(diagonalSum(matrix))