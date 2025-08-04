# 입력 받기
N = int(input())
# 입력값 저장하기
n_list = []
# 반복해서 입력된 숫자까지 0 ~ N까지 리스트에 저장하기 
for n in range(N + 1):
    n_list.append(n)
# 거꾸로 출력하기
for i in n_list[::-1]:
    print(i, end = ' ')

