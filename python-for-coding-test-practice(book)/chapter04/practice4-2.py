# Source: "This Is Coding Test with Python", Chapter 4-2 (Example Problem)
# Simulation Practice – Counting Time Containing Digit '3'

# This program counts how many times contain the digit '3'
# in a clock from 00:00:00 to N:59:59.

# Input:
# n: the ending hour (0 <= n <= 23)
n = int(input())

count = 0  # Number of times that include the digit '3'

# Iterate through all possible times
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            # Convert the time to a string and check if it contains '3'
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

# Output the result
print(count)
