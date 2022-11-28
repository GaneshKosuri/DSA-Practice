# --EASY--
# https://leetcode.com/problems/sqrtx/description/

# Solution starts
def mySqrt(x):
    start = 1
    end = x
    while(start < end):
        mid = (start+end)//2
        if(mid * mid == x):
            return mid
        if(mid*mid > x):
            end = mid - 1
        else:
            start = mid + 1
    return start if(start*start <= x) else start-1
# Solution ends

number = int(input("Enter a number: "))
print(mySqrt(number))