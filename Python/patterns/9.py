size = int(input("Enter Size: "));
for row in range(0,size):
    print(" "*row,end="")
    for column in range(0,2*(size-row)-1):
        print("*",end='')
    print()