T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    i = 0
    j = 0

    while i < N and j < M:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == N:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')