# --EASY--
# https://leetcode.com/problems/shuffle-the-array/description/

# Solution starts

def shuffle(nums, n):
    new_Array = []
    for i in range(n):
        new_Array.append(nums[i])
        new_Array.append(nums[n+i])
    return new_Array

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(shuffle(array,size//2))