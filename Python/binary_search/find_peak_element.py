# --MEDIUM--
# https://leetcode.com/problems/find-peak-element/description/

def findPeakElement(arr):
    start = 0
    end = len(arr) -1
    while(start < end):
        middle_index = start + (end - start)//2
        if(arr[middle_index] > arr[middle_index+1]):
            end = middle_index
        else:
            start = middle_index + 1
    return start

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(findPeakElement(array))
