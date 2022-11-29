# --EASY--
# https://leetcode.com/problems/arranging-coins/description/

def arrangeCoins(n) :
    start = 0
    end = n
    while start < end:
        mid = start + (end-start)// 2
        bound_one = mid * (mid + 1) // 2
        bound_two = (mid + 1) * (mid + 2) // 2
        if bound_one <= n < bound_two:
            return mid
        elif n < bound_one:
            end = mid - 1
        else:
            start = mid + 1
    return start

# For Demo purpose
number = int(input("Enter Number : "))
print(arrangeCoins(number))