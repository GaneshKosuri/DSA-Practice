# --EASY--
# https://leetcode.com/problems/number-of-good-pairs/


# Solution starts
def numIdenticalPairs(nums):
    good_pairs_count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] == nums[j]):
                good_pairs_count += 1
    return good_pairs_count

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(numIdenticalPairs(array))