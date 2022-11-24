# --EASY--
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Solution starts

def kidsWithCandies(candies, extraCandies):
    maximum = max(candies)
    return [candie + extraCandies >= maximum for candie in candies]

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
extra_candies = int(input("Enter extra candies: "))
print(kidsWithCandies(array,extra_candies))