
'''
# 두 개의 문자열 s1과 s2. s1의 각 글자가 s2에 모두 존재하는가?
A = 'XYPV'
B = 'EOGGXYPVSY'

result = True
for a in A:
    if a not in B:
        result = False
        break
print(result) # True

s1 = set(A)
s2 = set(B)

print(s1.issubset(s2)) # True
'''
'''
# 첫 줄에 N, 다음에 N*N 문자열. 'Z'가 존재하는가?
N = 5
arr = [['GOFFA'],
       ['OYECR'],
       ['UJAJQ'],
       ['JAEZN'],
       ['WJAKC']]
result = False

for r in range(N):
    if 'Z' in arr:
        result = True
        break
print(result) # False
'''
'''
# 첫 줄에 N, 다음에 N*N 지도, # 집중호우 피해구역. 피해구역 수는?
N = 5
arr = [
    ['000#0'],
    ['00###'],
    ['000#0'],
    ['00#00'],
    ['000#0']
]

damage_count = 0
for row in arr:
    for char in row[0]:
        if char == '#':
            damage_count += 1
print(damage_count)

damage_count = 0
for row in arr:
    damage_count += row[0].count('#')
print(damage_count)

'''
'''
# A와 B의 글자를 차례로 늘어놓기

A = 'XYPV'
B = 'EOGGXYPVSY'

N = len(A)
M = len(B)

result = []
i = j = 0 # 지금까지 처리된 문자 수

while i< N or j < M:
    if i < N:
        result.append(A[i])
        i += 1
    if j < M:
        result.append(B[j])
        j += 1
print(''.join(result)) # XEYOPGVGXYPVSY
'''
'''
# 첫 줄에 N, 다음에 N*N문자열. AB/CD 패턴이 존재하는가?



def find_2x2_pattern(grid, N, pattern):
    """
    주어진 격자에서 특정 2x2 패턴을 찾습니다.
    :param grid: N x N 문자열 리스트
    :param N: 격자의 크기
    :param pattern: ['AB', 'CD'] 형태의 2x2 패턴
    :return: 패턴이 존재하면 True, 아니면 False
    """
    if N < 2:
        return False
    
    for row in range(N-1):
        for col in range(N-1):
            top_left = grid[row][col]
            top_right = grid[row][col+1]
            bottom_left = grid[row+1][col]
            bottom_right = grid[row+1][col+1]
        
            if (top_left == pattern[0][0] and
                top_right == pattern[0][1] and
                bottom_left == pattern[1][0] and
                bottom_right == pattern[1][1]):
                return True
    
    return False

N = 5
arr = ['GOFFA',
       'OYECR',
       'UJAJQ',
       'JAEZN',
       'WJAKC']

target_pattern = ['GO', 'OY']

exists = find_2x2_pattern(arr, N, target_pattern)

print(exists)
'''

# 첫 줄에 N, 다음에 N*N 미로. 0 통로, 1 벽, # 로봇. 상하좌우로 모두 이동할 수 있는 칸은?
N = 5
arr = ['00101', 
       '1#101', 
       '00000', 
       '11010', 
       '00010']

# 방향 벡터
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 정답 카운터
ans = 0

for i in range(1, N-1):
    for j in range(1, N-1):
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if arr[ni][nj] == '1':
                break
        else:
            ans += 1
print(ans)
