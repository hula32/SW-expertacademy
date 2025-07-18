'''
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

# [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d, m, y, sep = '-')
'''
# 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
a = map(int,input().split('-'))
print(a, sep = '')

