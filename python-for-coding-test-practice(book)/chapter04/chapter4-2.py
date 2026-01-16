# Source: "This Is Coding Test with Python", Chapter 4-2 (Practice Problem)
# Simulation Practice – Knight's Possible Moves
#
# Given the starting position of a knight on a chessboard,
# this program calculates the number of valid moves the knight can make.

# Input:
# input_data: chess position in algebraic notation (e.g., "a1")
input_data = input()

# Convert column (a-h) to x-coordinate (1-8)
x = ord(input_data[0]) - ord('a') + 1

# Convert row (1-8) to y-coordinate
y = int(input_data[1])

# All possible moves of a knight (8 directions)
dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, 1, 2, -1, -2, -1, -2]

count = 0  # Number of valid moves

# Check each possible move
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    # Count the move if it stays within the chessboard
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

# Output the result
print(count)
