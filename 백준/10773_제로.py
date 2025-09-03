import sys
input = sys.stdin.readline

K = int(input())

stack = []

for k in range(K):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))