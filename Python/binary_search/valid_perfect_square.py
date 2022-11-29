# --EASY--
# https://leetcode.com/problems/valid-perfect-square/

# Solution ends

def isPerfectSquare(num):
    start = 1
    end = num
    if (num < 2):
        return True
    while(start <= end):
        mid = start + (end-start)//2
        mid_square = mid*mid
        if(mid_square == num):
            return True
        if(mid_square > num):
            end = mid - 1
        else:
            start = mid + 1
    return False

# Solution ends

size = int(input("Enter the number: "))
print(isPerfectSquare(size))