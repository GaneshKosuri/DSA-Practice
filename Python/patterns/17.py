size = int(input("Enter Size: "));
for row in range(0,2*size):
    spaces = size-row-1 if row < size else row-size
    print("  "*spaces,end="")
    totalColumns = 2*row if row <= size else 2*size-row
    for column in range(0,totalColumns+1):
            print("* ",end="")
    print()