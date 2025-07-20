
# 6001 : [기초-출력] 출력하기01
print("Hello")

# 6002 : [기초-출력] 출력하기02
print("Hello World")

# 6003 : [기초-출력] 출력하기03
print("Hello")
print("World")

# 6004 : [기초-출력] 출력하기04
print("\'Hello\'")

# 6005 : [기초-출력] 출력하기05
print('"Hello World"')

# 6006 : [기초-출력] 출력하기06
print('\"!@#$%^&*()\'')

# 6007 : [기초-출력] 출력하기07
print('"C:\\Download\\\'hello\'.py"')

# 6008 : [기초-출력] 출력하기08
print('print("Hello\\nWorld")')

# 6009 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기
c = input()
print(c)

# 6010 : [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기
n = int(input())
print(n)

# 6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기
f = float(input())
print(f)

# 6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기
a = int(input())
b = int(input())
print(a)
print(b)

# 6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기
a = str(input())
b = str(input())
print(b)
print(a)

# 6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기
f = float(input())
print(f)
print(f)
print(f)

# 6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기
a, b = map(int,input().split())
print(a)
print(b)

# 6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기.
a, b = (input().split())
print(b, a)

# 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기
s = input()
print(s, s, s)

# 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기
a, b = (input().split(':'))
print(a, b, sep =':') 

# 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d, m, y, sep = '-')

# 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
a, b = input().split('-')
print(a + b, sep='')

# 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기
h, m, s = input().split(':')
print(m)

# 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()
s = w1 + w2
print(s)

# 6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기
a, b = input().split()
c = int(a) + int(b)
print(c)

# [기초-값변환] 실수 2개 입력받아 합 계산하기
a = float(input())
b = float(input())
print(a + b)

# 6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기
n = int(input())
print('%x' %n)

# 6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기
n = int(input())
nums = str('%x' % n)
print(nums.upper())

# 6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기
n = int(input(), 16)
print('%o' % n)

# 6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기
n = ord(input())
print(n)

# 6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))

# 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n)

# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기
n = ord(input())
print(chr(n + 1))

# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기
a, b = map(int,input().split())
print(a - b)

# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기
a, b = map(float,input().split())
print(a * b)

# 6036 : [기초-산술연산] 단어 여러 번 출력하기
w, n = input().split()
print(w * int(n))

# 6037 : [기초-산술연산] 문장 여러 번 출력하기
n = int(input())
s = input()
print(s * n)

# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기
a, b = map(int, input().split())
print(a ** b)

# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
a, b = map(float, input().split())
print(a ** b)

# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기
a, b = map(int, input().split())
print(a // b)

# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기
a, b = map(int, input().split())
print(a % b)

# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(f'{a:0.2f}')

# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기
a, b = map(float,input().split())
c = a / b
print(f'{c:.3f}')

# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기
a, b = map(int,input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(f'{a / b:.2f}')

# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
a, b, c = map(int,input().split())
d = a + b + c
e = f'{(a + b + c)/3:.2f}'
print(d, e)

# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a << 1)

# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
a, b = map(int,input().split())
print(a << b)

# 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기
a, b = map(int,input().split())
print(a < b)

# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기
a, b = map(int,input().split())
print(a == b)

# 6050 : [기초-비교연산] 정수 2개 입력받아 비교하기
a, b = map(int,input().split())
print(a <= b)
