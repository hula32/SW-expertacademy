# 암호생성기

T = 10 # 테스트 케이스의 수는 10개로 고정

for tc in range(1, T+1):
    input() # 테스트케이스 번호는 무시
    # 따로 덱을 만들지 않고 리스트를 그대로 큐로 사용
    # 삽입: append, 삭제: pop(0)
    arr = list(map(int, input().split()))

    cnt = 1 # 감소시킬 숫자 1부터 시작 => 5까지 증가(1 사이클)
    
    # 언제까지 반복할지 모름 => 일단 무한루프를 돌고
    # 조건이 만족하는 경우에 while문을 빠져나온다.
    while True:
        # 숫자에서 cnt만큼 빼고 뒤로 보낸다
        num = arr.pop(0) # 큐의 맨 앞의 수 꺼내기
        num -= cnt

        if num <= 0: # 만약에 cnt만큼 뺐는데 음수가 나온다면
            arr.append(0)
            break # while문을 빠져나간다

        arr.append(num) # cnt만큼 뺀 수를 맨 뒤에 넣는다
        cnt += 1

        # 만약 cnt 5까지 빼고 나면 1부터 다시 시작해야 함.
        if cnt == 6: # 만약 cnt가 6이라면 5까지 수를 뺐다는 뜻이므로
            cnt = 1 # cnt를 1로 초기화
    
    arr = [str(a) for a in arr] # 숫자의 배열을 문자열의 배열로 바꾸고
    print(f"#{tc} {' '.join(arr)}")