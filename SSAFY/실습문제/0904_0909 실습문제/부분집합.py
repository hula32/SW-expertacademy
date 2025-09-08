# # 3명의 친구 부분집합 찾기
# arr = ['O', 'X']
# name = ['Min', 'Co', 'Tim']
# path = []

# def recur(cnt):
#     # 종료조건(3명을 모두 고려)
#     if cnt == 3:
#         print(*path)
#         return
    
#     # 재귀호출 파트
#     # - 부분집합에 포함되는 경우(O을 추가)
#     path.append(arr[0])
#     recur(cnt + 1)
#     path.pop()

#     # - 포함되지 않는 경우(X를 추가)
#     path.append(arr[1])
#     recur(cnt + 1)
#     path.pop()

# recur(0)

# '''
# O O O
# O O X
# O X O
# O X X
# X O O
# X O X
# X X O
# X X X

# '''
# # 반복문으로 작성해도 되지만 2~3번 정도는 그냥 작성하는게 가독성이 더 높기 때문에
# # 이렇게 풀어서 작성

# # ----------------------------- 실제로 많이 보는 코드 -> 이 코드 잘 이해하기!!!

# name = ['Min', 'Co', 'Tim']

# # 두 번째 선택에서는
# # 'Min' 이라는 친구가 포함된 상태를 저장하면서 
# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return
    
#     # 부분집합에 포함시키는 경우
#     recur(cnt + 1, subset + [name[cnt]])

#     # 포함시키지 않는 경우
#     recur(cnt + 1,  subset)

# recur(0, [])

# '''
# Min Co Tim
# Min Co
# Min Tim
# Min
# Co Tim
# Co
# Tim

# subset + [name[cnt]]
# subset

# 이 두가지는 같은 객체일까 아닐까?
# 왜 다를까? 새로운 리스트를 만들어서 리스트업 
# 그냥 '+' 쓸 때와 '+=' 쓸 때 주의!!
# '''

name = ['Min', 'Co', 'Tim']

def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return

    recur(cnt + 1, subset + [name[cnt]])

    recur(cnt + 1, subset)
    
    
recur(0, [])
    