T = int(input())

for t in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))

# N, min, max = 10, 1, 4
# scores = [1, 1, 2, 3, 5, 5, 4, 5, 6, 7]

    min_diff = 9999999

    for score1 in range(1, 101):
        for score2 in range(score1, 101):

            print(f"=== {score1}, {score2} ===")

            cls_cnt = [0] * 3
            #cls_cnt[0] 부진
            #cls_cnt[1] 보통
            #cls_cnt[2] 우수

            for score in scores:
                if score < score1:
                    cls_cnt[0] += 1
                elif score < score2:
                    cls_cnt[1] += 1
                else:
                    cls_cnt[2] += 1
            
            print(f"부진 분반 학생 수: {cls_cnt[0]}")
            print(f"보통 분반 학생 수: {cls_cnt[1]}")
            print(f"우수 분반 학생 수: {cls_cnt[2]}")
            print('===')

            for i in range(3):
                if cls_cnt[i] < min or cls_cnt[i] > max:
                    break
            else:
                max_cnt = 0
                min_cnt = 99999999
                for i in range(3):
                    if cls_cnt[i] > max_cnt:
                        max_cnt = cls_cnt[i]
                    if cls_cnt[i] > min_cnt:
                        min_cnt = cls_cnt[i] 
                result = max_cnt - min_cnt
                if result < min_diff:
                    min_diff = result
    if min_diff == 9999999:
        print(f'#{t} -1')
    else:
        print(f'{t} {min_diff}')        





