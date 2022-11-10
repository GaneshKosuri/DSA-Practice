size = int(input("Enter Size: "));
for row in range(0,size):
    spaces = size-row-1
    print(" "*spaces,end="")
    for column in range(0,2*row+1):
        print("*",end='')
    print()