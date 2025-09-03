N = 5
data = [1, 4, 7, 8, 0]

for i in range(N-1): # 0,1,2,3
    min_max = i
    for j in range(i+1, N): # 1~4, 2~4, 3~4, 4
        if data[min_max] > data[j]: # dats[min_max] : 1,4,7,8
            min_max = j # 4
    data[i], data[min_max] = data[min_max], data[i] #data[i]: 1,4,7,8, data[min_max]: 0,0,0,0
    # print(min_max) # 4,4,4,4
    # print(data[i]) # 0,1,4,7
    print(data[min_max]) # 1,4,7,8
# print(data)