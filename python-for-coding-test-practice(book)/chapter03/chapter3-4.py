# Source: "This Is Coding Test with Python", Chapter 3-4 (Practice Problem)
# Greedy Algorithm Practice – Until It Becomes 1

# Strategy:
# Repeatedly reduce n to 1 using the minimum number of operations.
# If n is divisible by m, divide it by m.
# Otherwise, subtract 1 from n.

# Input:
# n: initial number
# m: divisor
n, m = map(int, input().split())

count = 0  # Number of operations performed

# Continue until n becomes 1
while n != 1:
    if n % m != 0:
        n -= 1
        count += 1
    else:
        n //= m  # Integer division to keep n as an integer
        count += 1

# Output the total number of operations
print(count)
