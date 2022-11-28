
rows = 4
columns = 4
total_sum = 0
indices_array = []
for i in range(rows):
    for j in range(columns):
            bottom = a[i+1][j] if(i<rows-1 and [i+1,j] not in indices_array) else 0
            left = a[i][j-1] if(j>0 and [i,j-1] not in indices_array) else 0
            total_sum = left+right+top+bottom
            if(j<columns):
                indices_array.append([i,j+1])
            if(i>0):
                indices_array.append([i-1,j])
            if(i<rows-1):
                indices_array.append([i+1,j])
            if(j>0):
                indices_array.append([i,j-1])