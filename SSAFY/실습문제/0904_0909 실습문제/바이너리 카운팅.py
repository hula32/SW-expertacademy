 # 비트 연산자
# arr = [1, 2, 3, 4]

# # i : 0!2^n == i 번째 부분집합 
# for i in range(1 << len(arr)):  # 부분집합 번호
#     for idx in range(len(arr)):  # 각 원소들을 모두 확인
#         # i : 부분집합 번호 (각 자리의 포함 여부)
#         # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
#         if i & (1 << idx):
#             print(arr[idx], end=" ")
#     print()

# # 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
# def get_sub(tar):
#     print(f'target = {tar}', end = '/')
#     for i in range(len(arr)):
#         # 0x1로 표기한 이유(사실 1, 0b1, 0b0001, True 다 된다)
#         # - 비트 연산임을 명시하는 권장 방법
#         if tar& 0x1: # 가장 우측 비트를 체크
#             print(arr[i], end = ' ')
#             tar >>= 1

# for target in range(1 << len(arr)):
#     get_sub(target)
#     print()

'''
1 
2
1 2
3
1 3
2 3
1 2 3
4
1 4
2 4
1 2 4
3 4
1 3 4
2 3 4
1 2 3 4
target = 0/
target = 1/1
target = 2/
target = 3/1 2
target = 4/
target = 5/1
target = 6/
target = 7/1 2 3
target = 8/
target = 9/1
target = 10/
target = 11/1 2
target = 12/
target = 13/1
target = 14/
target = 15/1 2 3 4
'''


arr = [1, 2, 3, 4]

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end = ' ')
    print()

def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(len(arr)):
        if tar & 0x1:
            print(arr[i], end = ' ')
        tar >>=1

for target in range(1 << len(arr)):
    get_sub(target)
    print()