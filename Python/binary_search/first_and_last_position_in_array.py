# --MEDIUM--
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def binary_search(nums, target, startIndex):
    ans = -1
    start = 0
    end = len(nums) - 1
    while(start <= end):
        mid_index = start + (end-start)//2
        if(nums[mid_index] == target):
            ans = mid_index
            if(startIndex):
                end = mid_index - 1
            else:
                start = mid_index + 1
        elif(nums[mid_index] > target):
            end = mid_index - 1
        else:
            start = mid_index + 1
    return ans

def searchRange(nums, target):

    ans = [-1,-1]
    ans[0] = self.binary_search(nums,target,True)
    if(ans[0] != -1):
        ans[1] = self.binary_search(nums,target,False)
        
    return ans

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(input("Enter the letters separated by space : ").strip().split())[:size]
array = sorted(array)
element = int(input("Enter an element to search: "))
print(searchRange(array,element))
