# Source: "This Is Coding Test with Python", Chapter 3-2 (Practice Problem)
# Greedy Algorithm Practice (The Law of Large Numbers)
# This solution uses a repeating pattern to compute the maximum sum efficiently
# without iterating m times.

# Input:
# n: number of elements
# m: total number of additions
# k: maximum number of times the largest number can be added consecutively
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# Sort the list to identify the largest and second largest values
data.sort()
largest = data[n - 1]
second_largest = data[n - 2]

# The sequence repeats every (k + 1) operations:
# [largest repeated k times] + [second_largest once]
pattern_sum = largest * k + second_largest

# Number of full repeating patterns
pattern_count = m // (k + 1)

# Remaining additions after full patterns
remaining = m % (k + 1)

# Calculate the final result
result = 0
result += pattern_count * pattern_sum
result += remaining * largest

# Output the result
print(result)
