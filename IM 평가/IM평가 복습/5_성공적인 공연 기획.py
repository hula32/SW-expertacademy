T = int(input())

for t in range(1, T+1):
    person = input() # 110011

    hire = 0 # 고용할 사람
    cnt = 0 # 현재 박수 치는 사람

    for i, count_idx in enumerate(person):
        person_num = int(count_idx)
        if cnt < i: # 박수 최소 인원보다 작으면
            cnt_num = i - cnt
            hire += cnt_num
            cnt += cnt_num
        cnt += person_num


    print(f'#{t} {hire}')



