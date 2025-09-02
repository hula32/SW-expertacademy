T = int(input())

for t in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))

    min_diff = 999999 # 모든 score1, score2 조합 중 최소 학생수 차이

    for score1 in range(1, 11):
        for score2 in range(score1, 11):
            print(score1, score2, "조합 고려하기")
            # (1, 1), (1, 2), (1, 3), .. (1, 100)
            #         (2, 2), (2, 3), .. (2, 100)
            #                 (3, 3), .. (1, 100)
            #                           ...
            #                            (100, 100)


            cls_stu = [0] * 3 # 각 분반의 학생수

            for s in scores:
                if s < score1:
                    cls_stu[0] += 1  # [0] : 부진분반 학생수
                elif s < score2:
                    cls_stu[1] += 1  # [1] : 보통
                else:
                    cls_stu[2] += 1  # [2] : 우수

            print(cls_stu)

            for i in range(3): # 0, 1, 2 세 분반을 검사
                if cls_stu[i] < min or cls_stu[i] > max: # 만약 범위를 벗어나면
                    print(i, "분반의 학생수가 범위를 벗어났어요.")
                    break # 해당 조합 (score1, score2)은 볼 필요 없음
            else: # 위 for문에서 break가 안됐다면, 모든 반이 조건을 만족
                print("모든 반이 조건 만족")
                max_val = 0 # 최댓값을 찾기 위해 최소값으로 초기화
                min_val = 999999 # 최소값을 찾기 위해 최대값으로 초기화

                for i in range(3): # 0, 1, 2 세 분반중에서 최대, 최소 찾기
                    if cls_stu[i] < min_val:
                        min_val = cls_stu[i]
                    if cls_stu[i] > max_val:
                        max_val = cls_stu[i]

                diff = max_val - min_val # 최대 분반 - 최소 분반 = (score1, score2)로 나눴을 때 학생 수 차이
                print(f"diff: {diff}, min_diff: {min_diff}")             
                if min_diff > diff: # diff 중에서도 최소 구하기
                    min_diff = diff
    if min_diff == 999999:
        print(f'#{t} -1')
    else:
        print(f'#{t} {min_diff}')
                    

