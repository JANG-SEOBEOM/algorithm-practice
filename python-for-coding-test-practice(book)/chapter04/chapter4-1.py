input_data = input()
x = int(ord(input_data[0]) - ord('a')) + 1
y = int(input_data[1])

dx = [2,1,-2,-1,2,1,-2,-1]
dy = [1,2,1,2,-1,-2,-1,-2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if(nx <= 8 and nx >=1 and ny <= 8 and ny >=1):
        count += 1
    
print(count)