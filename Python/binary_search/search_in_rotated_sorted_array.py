# --MEDIUM--
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

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

def binary_Search(nums,target, start,end):
    while(start <= end):
        middle_index = start + (end - start)//2
        if(nums[middle_index] == target):
            return middle_index
        elif(nums[middle_index] > target):
            end = middle_index - 1
        else:
            start = middle_index + 1
    return -1
    


def search( nums, target):
    pivot_index = find_pivot_index(nums)
    if(pivot_index == -1):
        return binary_Search(nums,target,0,len(nums)-1)
    if(nums[pivot_index] == target):
        return pivot_index
    if(target >= nums[0]):
        return binary_Search(nums,target,0,pivot_index-1)
    else:
        return binary_Search(nums,target,pivot_index+1,len(nums)-1)

size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
target = int(input("Enter target : "))
print(search(array,target))
