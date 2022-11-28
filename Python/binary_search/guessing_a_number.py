# --EASY--
# https://leetcode.com/problems/guess-number-higher-or-lower/description/

def guessNumber(self, n: int) -> int:
    start = 1
    end = n
    while(start < end):
        mid = start+ (end-start)//2
        guess_check = guess(mid)
        if(not guess_check):
            return mid
        if(guess_check == -1):
            end = mid - 1
        else:
            start = mid + 1
    return start
