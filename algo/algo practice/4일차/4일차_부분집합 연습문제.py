# def print_subset(bit):
# 	for i in range(4):
# 			if bit[i]:  # bit[i]가 0이 아니면
# 				print(arr[i], end = ' ')
# 	print(bit)

# arr = [7, 5, 8, 1]

# bit = [0, 0, 0, 0]
# for i in range(2):
# 	bit[0] = i # 0번 원소
# 	for j in range(2):
# 			bit[1] = j  # 1번 원소
# 			for k in range(2):
# 					bit[2] = k  # 2번 원소
# 					for l in range(2):
# 							bit[3] = l  # 3번 원소
# 							print_subset(bit)


# # # 연습문제 3

# T = list(map(int, input().split()))


arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수 -> n개의 원소 => 2^n 개의 부분집합 / 0부터 2^n -1이 자동으로 만들어짐
	for j in range(n): # 원소의 수만큼 비트를 비교함
			if i & (1<<j): # i의 j번 비트가 1인 경우
					print(arr[j], end = ",") # j번 원소 출력 
	print(f' : {i:06b}')
print()