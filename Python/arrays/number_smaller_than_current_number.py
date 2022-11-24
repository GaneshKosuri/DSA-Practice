# --EASY--
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


# Solution starts
def smallerNumbersThanCurrent(nums):
    new_array = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if(i==j):
                continue
            elif(nums[i]>nums[j]):
                count += 1
        new_array.append(count)
    return new_array

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(getConcatenation(array))