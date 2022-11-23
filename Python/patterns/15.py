size = int(input("Enter Size: "));
for row in range(0,2*size):
    spaces = size-row if row <= size else row-size
    print(" "*spaces,end="")
    totalColumns = row if row <= size else 2*size-row
    for column in range(0,totalColumns):
        if (column == 0 or column == totalColumns-1):
            print("* ",end='')
        else:
            print("  ",end="")
    print()