# --EASY--
# https://leetcode.com/problems/running-sum-of-1d-array/description/

# Solution starts
def runningSum(nums):
    new_array = [nums[0]]
    for i in range(1,len(nums)):
        new_array.append(new_array[i-1]+nums[i])
    return new_array
# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(runningSum(array))