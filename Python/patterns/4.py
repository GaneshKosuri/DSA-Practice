size = int(input("Enter Size: "));
for row in range(1,size+1):
    for column in range(1,row+1):
        print(column,end=' ')
    print()