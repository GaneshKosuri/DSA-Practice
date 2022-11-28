# --EASY--
# https://leetcode.com/problems/find-the-highest-altitude/description/

# Solution starts
def largestAltitude(gain ):
    altitude_matrix = [0]
    for i in range(len(gain)):
        new_altittude = altitude_matrix[i] + gain[i]
        altitude_matrix.append(new_altittude)
    return max(altitude_matrix)
# SOlutoin ends

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
print(largestAltitude(array))