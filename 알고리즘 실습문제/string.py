# A와 B의 글자를 차례로 늘어놓기
A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0

ans = [0] * (N + M)
while i+j < N+M:
    if i < N:
        ans[i+j] = A[i]
        i += 1

    if j < M:
        ans[i+j] = B[j]
        j += 1

print(*ans)


