size = int(input("Enter Size: "));
for row in range(0,size):
    spaces = size-row-1
    print(" "*spaces,end="")
    for column in range(0,row+1):
        if (column == 0 or column == row or row == size-1):
            print("* ",end='')
        else:
            print("  ",end="")
    print()