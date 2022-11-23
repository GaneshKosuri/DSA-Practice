size = int(input("Enter Size: "));
for row in range(0,2*size):
    spaces = row if row < size else 2*size-row-1
    print(" "*spaces,end="")
    totalColumns = size-row if row< size else row-size+1
    for column in range(0,totalColumns):
        print("* ",end='')
    print()