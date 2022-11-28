# --EASY--
# https://leetcode.com/problems/add-to-array-form-of-integer/description/

# Solution starts

def addToArrayForm(num, k):
    sum = num[0]
    for i in range(1,len(num)):
        sum *= 10
        sum += num[i]
    sum += k
    return [x for x in str(sum)]

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
element_to_add = int(input("Enter element to add : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(addToArrayForm(array,element_to_add))