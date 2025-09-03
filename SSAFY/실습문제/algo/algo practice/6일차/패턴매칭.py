
t = 'TTTTAACCA'
p = 'TTAT'

def brute_force(p, t): # 찾을 패턴, 본문 문자열
    i = 0
    j = 0
    
    N = len(t) # 9
    M = len(p) # 4
    while j < M and i < N:
        if t[i] != p[j]: # 현재 문자가 다르면
            i = i - j # 시작 위치로 돌아감 / 시작 위치를 한 칸 옮긴 셈
            j = -1 # 다음 줄에서 j+1 돼서 0으로 초기화
        i = i + 1
        j = j + 1
    if j == M:
        # j는 패턴 p에서 현재 비교 중인 문자 인덱스 
        # j가 M-1일 때 마지막 문자 비교를 하고, 다음 줄에서 j = j + 1을 해서
        # j가 M이 되면, → 패턴의 모든 문자 비교가 끝났다는 뜻
        return i - M # 본문에서 패턴이 처음 시작한 위치 / i는 마지막 비교가 끝난 다음 본문 인덱스가 나옴
    else:
        return -1

print(brute_force(p, t))

'''
t[0] = T , p[0] = T
i = 1, j = 1

t[1] = T , p[1] = T
i = 2, j = 2

t[2] = T , p[2] = A # 불일치
i = i - j = 2 - 2 = 0
j = -1
아래  구간을 거쳐서 +1 돼서 
i = i + 1
j = j + 1
i = 1, j = 0

... 계속됨

패턴이 끝까지 일치(j == m) 하면 i - m 반환
'''

