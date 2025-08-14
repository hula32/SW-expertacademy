# 우수/보통/부진 점수를 기준으로 score1, score2를 임의로 선정하여 나눔
# score2 이상: 우수, score1이상 ~ score2미만 : 보통, score1 미만 : 부진
# 최소인원 min 이상, 최대인원 max 이하 만족
# 학생이 가장 많은 분반과 가장 적은 분반의 차 최솟값

T = int(input())

for t in range(1, T+1):
    N, min_v, max_v = map(int, input().split())
    scores = list(map(int, input().split()))

    min_result = 99999999

    for score1 in range(1, 101):
        for score2 in range(score1, 101):

            cls = [0] * 3
            # cls[0] = 부진
            # cls[1] = 보통
            # cls[2] = 우수

            for score in scores:
                if score < score1:
                    cls[0] += 1
                elif score < score2:
                    cls[1] += 1
                else:
                    cls[2] += 1
            
            for i in range(3):
                if cls[i] < min_v or cls[i] > max_v: # 영역에서 벗어나면
                    break
            else: # 영역에 있으면
                max_val = 0
                min_val = 9999999
                for i in range(3):
                    if cls[i] > max_val:
                        max_val = cls[i]
                    if cls[i] < min_val:
                        min_val = cls[i]
                result = max_val -min_val
                if min_result > result:
                    min_result = result

    if min_result == 99999999:
        print(f'#{t} -1')
    else:
        print(f'#{t} {min_result}')


