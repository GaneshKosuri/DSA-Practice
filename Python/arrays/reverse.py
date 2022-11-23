# Reversing an Array using two pointer method

def reverseArray(arr):
    startIndex = 0
    endIndex = len(arr) - 1
    while(startIndex < endIndex):
        arr[startIndex] , arr[endIndex] = arr[endIndex] , arr[startIndex]
        startIndex += 1
        endIndex -= 1
    print("Reversed Array",arr)


size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]

print('Original Array',array)
reverseArray(array)
