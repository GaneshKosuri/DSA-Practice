size = int(input("Enter Size: "));
for row in range(0,size):
    print(" "*row,end="")
    for column in range(0,size-row):
        if (row == 0 or column == 0 or column == size-row-1):
            print("* ",end='')
        else:
            print("  ",end="")
    print()