# Source: "This Is Coding Test with Python", Chapter 4-1 (Example Problem)
# Simulation Practice – Moving in Four Directions (Up, Down, Left, Right)

# The character starts at position (1, 1) on an N x N grid.
# Based on the movement plans, update the position while
# ensuring the character does not move outside the grid.

# Input:
# n: size of the grid (n x n)
n = int(input())

# List of movement commands
plans = input().split()

# Starting position
x, y = 1, 1

# Movement types and corresponding coordinate changes
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]   # Change in x for each move
dy = [-1, 1, 0, 0]   # Change in y for each move

# Process each movement plan
for plan in plans:
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]

    # Ignore the move if it goes outside the grid
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    # Update the current position
    x, y = nx, ny

# Output the final position
print(x, y)
