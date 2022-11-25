# --EASY--
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def nextGreatestLetter(letters, target) :
    start = 0
    end = len(letters) - 1
    while(start <= end):
        middle_index = start + (end-start)//2
        if(letters[middle_index] > target):
            end = middle_index - 1
        else:
            start = middle_index + 1
    return letters[0] if (start >= len(letters)) else letters[start]

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(input("Enter the letters separated by space : ").strip().split())[:size]
array = sorted(array)
element = int(input("Enter an element to search: "))
print(nextGreatestLetter(array,element))
