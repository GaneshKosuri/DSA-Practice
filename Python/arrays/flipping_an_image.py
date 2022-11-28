# --EASY--
# https://leetcode.com/problems/flipping-an-image/description

# Solution starts
def flipAndInvertImage(image ):
    new_array = []
    size = len(image)
    for row in range(size):
        updated_row = []
        for column in range(size-1,-1,-1):
            data = 0 if(image[row][column]) else 1
            updated_row.append(data)
        new_array.append(updated_row)
    return new_array
# Solution ends

# For Demo purpose
size = int(input("Enter n x n matrix Size : "))
accounts = []
for i in range(0,size):
    accounts.append(list(map(int,input("Enter the binary numbers separated by space for row {} : ".format((i+1))).strip().split()))[:size])
print(flipAndInvertImage(accounts))