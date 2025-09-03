'''
1번
김싸피는 시험점수를 관리하는 코드를 작성하려고한다.
전체점수 중 최저점을 반환하는 min_score 함수를 완성하시오.
Python 내장함수 min 사용시감점
'''
sample_scores = {
        "수학": 72,
        "국어": 45,
        "영어": 88,
        "과학": 59,
        "사회": 60,
        "체육": 47
    }
def min_score(scores):
    # 최대값을 찾으려면 max_val = 최소값으로 초기화
    # 최소값을 찾으려면 min_val = 최대값으로 초기화
    # 인자 sample_scores를 반복문을 돌 때 키 값이 이미 출력
    min_val = 100 # 999999
    for key in scores:
        if scores[key] < min_val:
            min_val = scores[key]
        else:
            pass
    return min_val

print(min_score(sample_scores))
'''
2번
김싸피는 시험점수를 관리하는 코드를 작성하려고한다.
전체점수 중 60점미만인 과목의 개수를 계산하여 반환하는 under_60 함수를 완성하시오.
'''
sample_scores = {
        "수학": 72,
        "국어": 45,
        "영어": 88,
        "과학": 59,
        "사회": 60,
        "체육": 47
    }
def under_60(scores):
    count = 0
    for key in scores:
        if scores[key] < 60:
            count = count + 1
        else:
            pass
    return count

print(under_60(sample_scores))

