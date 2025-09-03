# N명 손님
# M초 시간 -> K개

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, (input().split()))

    person = sorted(list(map(int, input().split())))

    cnt = 0
    result = "Possible"

    for i in range(person[-1]+1): # 0,1,2,3,4
        if (i+1) % M == 0:
            cnt += K
        if i == person[0]:
            if cnt > 0 :
                cnt -= 1
                person.pop(0)
            else:
                result = "Impossible"
                break
    
    print(f'#{t} {result}')
            



