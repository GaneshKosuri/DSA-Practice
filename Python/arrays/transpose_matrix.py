# --EASY--
# https://leetcode.com/problems/transpose-matrix/submissions/

# Solution starts
def transpose(matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    new_matrix = []
    for j in range(matrix_columns):
        row = []
        for i in range(matrix_rows):
            row.append(matrix[i][j])
        new_matrix.append(row)
    return new_matrix

# Solution ends

# For Demo purpose
rows = int(input("Enter matrix rows : "))
columns = int(input("Enter matrix columns : "))
matrix = []
for i in range(0,rows):
    matrix.append(list(map(int,input("Enter the numbers separated by space for row {} : ".format((i+1))).strip().split()))[:columns])
print(transpose(matrix))