# 점수별 우수/보통/부진
# score1, score2 점수를 토대로 선정
# score2 이상: 우수 분반 / score1 이상 ~ score2미만 : 보통 분반 / score1 미만: 부진 분밥
# min이상과 max이하를 만족해야함
# 학생이 가장 많은 분반 - 학생이 가장 적은 분반 학생  수 차의 최솟값
# 없다면 -1 출력

T = int(input())

for t in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))
    
    min_diff = 9999999

    for score1 in range(1, 101):
        for score2 in range(score1, 101):

            cls_cnt = [0] * 3

            for score in scores:
                if score < score1:
                    cls_cnt[0] += 1
                elif score < score2:
                    cls_cnt[1] += 1
                else:
                    cls_cnt[2] += 1
            
            for i in range(3):
                if cls_cnt[i] < min or cls_cnt[i] > max:
                    break
            else:
                min_cnt = 9999999
                max_cnt = 0
                for i in range(3):
                    if cls_cnt[i] < min_cnt:
                        min_cnt = cls_cnt[i]
                    if cls_cnt[i] > max_cnt:
                        max_cnt = cls_cnt[i]
                diff = max_cnt - min_cnt
                if min_diff > diff:
                    min_diff = diff

    if min_diff == 9999999:
        print(f'#{t} -1')
    else:
        print(f'#{t} {min_diff}')



    

