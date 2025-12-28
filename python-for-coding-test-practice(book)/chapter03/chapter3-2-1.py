# Source: "This Is Coding Test with Python", Chapter 3-2 (Practice Problem)
# Greedy Algorithm Practice:
# Find the maximum possible sum by adding numbers under repetition constraints.

# Input:
# n: number of elements
# m: total number of additions
# k: maximum number of times the largest number can be added consecutively
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# Sort the list to easily access the largest and second largest values
data.sort()
largest = data[n - 1]
second_largest = data[n - 2]

result = 0
count = 0  # Counter for consecutive additions of the largest number

# Add numbers according to the constraint
for _ in range(m):
    if count < k:
        result += largest
        count += 1
    else:
        result += second_largest
        count = 0

# Output the final result
print(result)