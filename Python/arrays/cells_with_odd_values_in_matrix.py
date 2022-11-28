# --EASY--
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

# Solution starts
def oddCells( m, n, indices):
    initial_matrix = [[0 for j in range(n)] for i in range(m) ]
    rows = [0 for i in range(m)]
    columns = [0 for j in range(n)]
    for increment_row in indices:
        row_index , column_index = increment_row
        rows[row_index] += 1
        columns[column_index] += 1
    odd_numbers_count = 0
    for i in range(m):
        for j in range(n):
            if((rows[i] + columns[j])%2 != 0):
                odd_numbers_count += 1
    return odd_numbers_count
# Solution ends

# Demo purpose
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
indices_matrix = [[0,1],[1,1]]
print(oddCells(rows,columns,indices_matrix))