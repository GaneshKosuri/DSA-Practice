size = int(input("Enter Size: "));
for row in range(0,2*size):
    columnSize = 2*size-row if (row > size) else row
    for column in range(0,columnSize):
        print("*",end=' ')
    print()