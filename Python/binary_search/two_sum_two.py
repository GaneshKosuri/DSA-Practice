# --MEDIUM--
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Solution ends

def twoSum( numbers, target) :
    start = 0
    end = len(numbers) - 1
    while(start < end):
        if(numbers[start]+numbers[end] == target):
            return [start+1,end+1]
        if(numbers[start]+numbers[end] < target):
            start += 1
        else:
            end -= 1
    return [start-1,end-1]

# Solution ends

size = int(input("Enter size of the array: "))
array = list(map(int,input("Enter number separated by space: ").strip().split()))[:size]
target = int(input("Enter target number: "))
print(twoSum(array, target))