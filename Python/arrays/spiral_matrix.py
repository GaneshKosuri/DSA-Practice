# --MEDIUM--
# https://leetcode.com/problems/spiral-matrix/


# Solution starts
def maximumWealth(accounts) -> int:
        maximum_wealth = 0
        for row in accounts:
            maximum_wealth = max(maximum_wealth,sum(row))
        return maximum_wealth

# Solution ends

# For Demo purpose
size = int(input("Enter Array Size : "))
accounts = []
for i in range(0,size):
    accounts.append(list(map(int,input("Enter the numbers separated by space for row {} : ".format((i+1))).strip().split()))[:size])
print(maximumWealth(accounts))