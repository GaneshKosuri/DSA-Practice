# --HARD--
# https://leetcode.com/problems/split-array-largest-sum/

def binary_search( nums,start, end,k):
    while(start < end):
        mid = start + (end - start)//2
        sub_arrays_count = 1
        sub_array_sum = 0
        for num in nums:
            if((sub_array_sum + num) > mid):
                sub_array_sum = num
                sub_arrays_count += 1
            else:
                sub_array_sum += num
        if(sub_arrays_count <= k):
            end = mid
        else:
            start = mid + 1
    return start




def splitArray( nums, k):
    minimum = max(nums)
    maximum = sum(nums)
    return binary_search(nums,minimum,maximum,k)

size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
sub_arrays_count = int(input("Enter sub arrays count: "))
print(splitArray(array,sub_arrays_count))