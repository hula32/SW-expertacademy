N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))

total = 0

while True: # total > M이 되면 멈추고 결과값 도출
    for i in range(0, len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                new_total = number[i] + number[j] + number[k]
                if new_total <= M:
                    if total < new_total:
                        total = new_total
    break

print(total)