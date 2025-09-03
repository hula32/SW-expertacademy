T = int(input())

for t in range(1, T+1):
    N = int(input())

    box = [0] * 301

    box[10] = 1
    box[20] = 3
    box[30] = 5

    for i in range(40, N+1):
        box[i] = box[i-10] + (box[i-20]*2)

    print(f'#{t} {box[N]}')
