T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()
    result = []

    for i in range(N//2+1):
        if len(result) >= 10:
            break
        result.append(numbers[-(i+1)])
        if len(result) >= 10:
            break
        result.append(numbers[i])

    print(f'#{t}', *result)
