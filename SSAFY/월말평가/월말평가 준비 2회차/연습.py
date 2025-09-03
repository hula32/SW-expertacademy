'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

V = int(input())
arr = list(map(int, input().split()))

lft_child = [0] * (V+1)
rgt_child = [0] * (V+1)

for i in range(V-1):
    parent, child = arr[2*i], arr[2*i + 1]
    print(parent, child)
    if lft_child[parent] == 0:
        lft_child[parent] = child
    else:
        rgt_child[parent] = child
print(lft_child)
print(rgt_child)

def f(root):
    print(root, end=' ')

    if lft_child[root] != 0:
        f(lft_child[root])
    if rgt_child[root] != 0:
        f(rgt_child[root])

def inorder(root):
    if lft_child[root] != 0:
        inorder(lft_child[root])
    print(root, end = ' ')
    if rgt_child[root] != 0:
        inorder(rgt_child[root])

def postorder(root):
    if lft_child[root] != 0:
        postorder(lft_child[root])
    if rgt_child[root]:
        postorder(rgt_child[root])
    print(root, end = ' ')

print("트리 전위순회 시작")
f(1) # 1번 노드를 중심으로 순회
print()
print("트리 전위순회 끝")

print("트리 중위순회 시작")
inorder(1) # 1번 노드를 중심으로 순회
print()
print("트리 중위순회 끝")

print("트리 후위순회 시작")
postorder(1) # 1번 노드를 중심으로 순회
print()
print("트리 후위순회 끝")
