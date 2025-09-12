arr = [1, 2, 2, 4, 2, 3, 4, 5, 6, 4, 3, 2, 4, 4, 5, 5]
K = 4

result = 0 # 3이되면 stop
for i in range(0, len(arr), K):
    new_arr = arr[i:i+K]
    cnt = 0
    for j in range(len(new_arr)-1):
        if new_arr[j] < new_arr[j+1]:
            cnt += 1
    if cnt == K-1:
            result += 1

print(result)
