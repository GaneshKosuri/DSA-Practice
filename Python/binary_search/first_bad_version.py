# --EASY--
# https://leetcode.com/problems/first-bad-version/description/

# Solution starts

def firstBadVersion(n) :
    start = 1
    end = n
    while(start < end):
        mid = start + (end - start)//2
        if(isBadVersion(mid)):
            end = mid
        else:
            start = mid + 1
    return end

# Solution ends

