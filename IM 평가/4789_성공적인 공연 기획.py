T = int(input())

for t in range(1, T+1):
    person = input() #110011

    count = 0 # 추가 고용할 사람의 수
    clap = 0 # 현재까지 박수 치고 있는 사람 총합

    for idx, count_idx in enumerate(person): # 0,1,2,3,4,5 -> 필요 인원수
        print(f'필요 명수 : {idx}, 해당 최소 인원을 가진 관객 수 : {count_idx}')
        person_num = int(count_idx)
        if idx > clap:
            need = idx - clap
            count += need
            clap += need
        clap += person_num
        

    print(f'#{t} {count}')
            

    
