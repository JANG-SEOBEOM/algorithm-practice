# Source: "This Is Coding Test with Python", Chapter 3-3 (Practice Problem)
# Greedy Algorithm Practice – Number Card Game

# Strategy:
# From each row, select the smallest number.
# Among those selected numbers, choose the largest one.

# Input:
# n: number of rows
# m: number of columns
n, m = map(int, input().split())

result = 0  # Stores the maximum value among the row minimums

# Process each row
for _ in range(n):
    data = list(map(int, input().split()))
    row_min = min(data)  # Minimum value in the current row

    # Update the result if the current row's minimum is larger
    if row_min > result:
        result = row_min

# Output the final result
print(result)