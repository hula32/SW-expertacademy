# 탐욕 알고리즘을 활용한 Baby-gin 접근
num = 456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] = c[num % 10] + 1 
    '''
    c[45678.9] -> c[9] + 1
    c[4567.8] -> c[8] + 1
    c[456.7] -> c[7] + 1
    c[45.6] -> c[6] + 1
    c[4.5] -> c[5] + 1
    c[4] -> c[4] + 1
    '''
    num //= 10
    '''
    45678
    4567
    456
    45
    4
    0
    '''
    print(num)

# 탐욕 알고리즘을 활용한 Baby-gin 접근
c = [4, 5, 6, 7, 8, 9]

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i] >= 1 and c[i] >= 1:
        c[i] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby jin")
else:
    print("Lose")

