# --MEDIUM--
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def find_pivot_index( nums):
    start = 0
    end = len(nums) - 1
    while(start <= end):
        middle_index = start + (end - start)//2
        if(middle_index < end and nums[middle_index] > nums[middle_index+1]):
            return middle_index
        if(middle_index > start and nums[middle_index] < nums[middle_index-1]):
            return middle_index - 1
        if(nums[middle_index] <= nums[start]):
            end = middle_index - 1
        else:
            start = middle_index + 1 
    return -1

def findMin( nums):
    pivot_index = find_pivot_index(nums)
    if(pivot_index == -1):
        return nums[0]
    else:
        return nums[pivot_index+1]
    

size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(findMin(array))
