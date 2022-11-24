# --EASY--
# https://leetcode.com/problems/create-target-array-in-the-given-order/description/

# Solution starts

def createTargetArray(nums, index):
    target_array = []
    for i in range(len(nums)):
        target_array.insert(index[i],nums[i])
    return target_array

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
nums_array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
index_array = list(map(int,input("Enter the indexes separated by space : ").strip().split()))[:size]
print(createTargetArray(nums_array,index_array))