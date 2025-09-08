# 중복 없는 순열
# [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.

path = []  # visited, used, ... --> 뽑은 카드들을 저장
# used = [False, False, False, False, False, False] # 고를 수 있는 수 만큼 만들어준다.
# used = [False] * N -> N개의 카드 종류가 있는 경우

used = [False] * 7 # 1~6까지의 카드 숫자 사용여부를 기록(0은 버린다)

def recur(cnt):
    if cnt == 3: # 기저조건
        print(*path)
        return
    
    for num in range(1, 7): # 유도조건
        # in을 쓰면 리스트 전부를 다 확인
        # if num in path: # 이미 path에 있는 숫자는 생략
        #     continue # 잠재적 위험 요소 : if 숫자 in 리스트 -> 시간이 오래 걸림
        if used[num]:
            continue

        used[num] = 1
        path.append(num)
        recur(cnt + 1)
        path.pop() 
        used[num] = 0

recur(0)