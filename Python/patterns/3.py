size = int(input("Enter Size: "));
for row in range(0,size):
    for column in range(0,size-row):
        print("*",end=' ')
    print()