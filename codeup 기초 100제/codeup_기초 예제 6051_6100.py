'''
# 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기
a, b = map(int,input().split())
print(a != b)

# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기
a = int(input())
print(bool(a))

# 6053 : [기초-논리연산] 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
a, b = map(int,input().split())
print(bool(a and b))

# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기
a, b = map(int,input().split())
print(bool(a or b))

# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기
a, b = map(int,input().split())
print(bool(((not a) and b) or ((not b) and a)))

# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
a, b = map(int,input().split())
print(bool(((not a) and (not b)) or (a and b)))

# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
a, b = map(int,input().split())
print(bool((not a) and (not b)))

# 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

# 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
a, b = map(int,input().split())
print(a & b)

# 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
a, b = map(int,input().split())
print(a | b)

# 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
a, b = map(int,input().split())
print(a ^ b)

# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기
a, b = map(int,input().split())
print(a if (a >= b) else b)

# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = map(int,input().split())
print((a if (a < b) else b) if ((a if (a < b) else b) < c) else c)

# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a, b, c = map(int,input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int,input().split())
if a % 2 == 0:
    print("even")
else :
    print("odd")
if b % 2 == 0:
    print("even")
else :
    print("odd")
if c % 2 == 0:
    print("even")
else :
    print("odd")

# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
a = int(input())
if (a < 0) and (a % 2 == 0) : 
    print('A')
elif (a < 0) and (a % 2 != 0):
    print('B')
elif (a >0) and (a % 2 == 0) : 
    print('C')
else :
    print('D')

# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
a = int(input())
if a >= 90 :
    print('A')
elif a >= 70 :
    print('B')
elif a >= 40 :
    print('C')
else :
    print('D')

# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else :
    print('what?')

# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
a = int(input())
if a // 3 == 1 :
    print('spring')
elif a // 3 == 2 :
    print('summer')
elif a // 3 == 3 :
    print('fall')
else :
    print('winter')

# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기
n = 1  #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n != 0 :
    n = int(input())
    if n != 0:
        print(n)
    else :
        break

# 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기
n = int(input())
while n != 0:
    print(n)
    n -= 1
    if n == 0 :
        break

# 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기
n = int(input())
while n != 0 :
    n -= 1
    print(n)
    if n == 0 :
        break

# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
n = ord(input())
t = ord('a')
while t <= n :
    print(chr(t), end = ' ')
    t += 1

# [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기
n = int(input())
nums = 0
while nums <= n :
    print(nums)
    nums += 1

# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기
n = int(input())
for i in range(n + 1) :
    print(i)

# 6077 : [기초-종합] 짝수 합 구하기 (for문)
n = int(input())
s = 0
for i in range(1, n + 1) :
    if i % 2 == 0 :
        s += i

print(s)

# 6077 : [기초-종합] 짝수 합 구하기(while문)
n = int(input())
s = 1
result = 0
while s <= n :
    if s % 2 == 0 :
        result += s
        s += 1
    else :
        s += 1    

print(result)
'''
# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(for문)
a = input()

for i in a != 'q' :
    print(i)
    if a == 'q' :
        print(a)
        break

