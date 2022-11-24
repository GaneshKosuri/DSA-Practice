# --EASY--
# https://leetcode.com/problems/concatenation-of-array/


# Solution starts

def getConcatenation(nums):
        array = nums
        for i in range(len(nums)):
            array.append(nums[i])
        return array

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(getConcatenation(array))