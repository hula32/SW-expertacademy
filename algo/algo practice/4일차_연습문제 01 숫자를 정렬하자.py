# 버블정렬
T = int(input())

def Bubble(a, n):
    for i in range(n-1, 0, -1): # 4,3,2,1
        for j in range(i): # 0~3,0~2,0~1 
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
    return " ".join(map(str, a))

for t in range(1, T+1):
    N = int(input())
    N_number = list(map(int, input().split()))

    result = Bubble(N_number, N)
    print(f'#{t} {result}')




