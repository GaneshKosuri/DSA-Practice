# --EASY--
# https://leetcode.com/problems/build-array-from-permutation/description/

# Solution starts

def buildArray(nums):
        return [nums[nums[index]] for index in range(len(nums))]

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(buildArray(array))