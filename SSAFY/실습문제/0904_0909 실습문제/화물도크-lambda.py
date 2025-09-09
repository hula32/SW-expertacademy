# lambda 함수
# - 일회용 함수
# - 짧음

# 람다 함수의 정의
# lambda  파라미터 : 반환값
# ex) lambda a, b: a + b

add = lambda a, b: a + b

# 일반 함수 정의와 비교
def add2(a, b):
    return a + b
# 1. def 키워드 대신 lambda 키워드
# 2. 함수명을 삭제, 파라미터 감싸는 괄호도 제거
# 3. return 키워드 제거
# 4. 한줄로 쓰기


# print(add(3, 5))

things =[(1,4), (3,5), (1,6), (3,8), (5,7), (5,9), (6,10), (8,11), (2,13), (12,14)]

key = lambda t: t[0]

# for t in things:
#     print(key(t))

front_nums = [key(t) for t in things]
print(front_nums)