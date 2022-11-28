# --EASY--
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Solution starts

def findNumbers(nums) -> int:
        even_digits_count = 0;
        for num in nums:
            if(len(str(num)) % 2 == 0):
                even_digits_count += 1
        return even_digits_count

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(findNumbers(array))