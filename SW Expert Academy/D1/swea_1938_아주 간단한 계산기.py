# 문제풀이 방법 1
a, b = map(int,input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)

# 문제풀이 방법 2
# list() : 반복가능한 것(여러 개의 요소가 있는 것)을 리스트로 만듬

nums = list(map(int,input().split()))
a, b = nums

print(a + b)
print(a - b)
print(a * b)
print(a // b)