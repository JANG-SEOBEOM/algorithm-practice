input_data = input()
x = int(input_data[0] - 'a')
y = int(input_data[1])

dx = [2,1,-2,-1,2,1,-2,-1]
dy = [1,2,1,2,-1,-2,-1,-2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if(nx < 8 and nx >=0 and ny < 8 and ny >=0):
        count += 1
    
print(count)