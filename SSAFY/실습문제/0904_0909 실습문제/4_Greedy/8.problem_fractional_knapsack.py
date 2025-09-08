# # [문제] fraction_knapsack
# n = 3
# target = 30  # Knapsack KG
# things = [(5, 50), (10, 60), (20, 140)]  # (Kg, Price)

# # kg 당 가격으로 어떻게 정렬 ?
# # 정렬 : (price / kg)
# # lambda: 재사용하지 않는 함수
# things.sort(key=lambda x: (x[1] / x[0]), reverse=True)

# print(things)

# total = 0
# for kg, price in things:
#     '''
#     [(5, 50), (20, 140), (10, 60)]
#     '''
#     per_price = price / kg

#     # 만약 가방에 남은 용량이 얼마되지 않는다면,
#     # 물건을 잘라 가방에 넣고 끝낸다.
#     if target < kg:
#         total += target * per_price
#         break

#     total += price
#     target -= kg

# print(int(total))


# n = 10
# things =[(1,4), (3,5), (1,6), (3,8), (5,7), (5,9), (6,10), (8,11), (2,13), (12,14)]

# things.sort(key=lambda x: x[1])

# '''
# [(1, 4), (3, 5), (1, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (2, 13), (12, 14)]
# '''


# result = []
# last_end = 0

# for start, end in things:
#     if start >= last_end:
#         result.append((start, end))
#         last_end = end

# print(result)
# print(len(result))


number = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(number)
path = []

def recur(idx, chosen):
    if idx == n:
        if len(chosen) >= 1 and sum(chosen) == 0:
            print(sum(chosen))
            print(chosen)
        return
    
    recur(idx + 1, chosen + [number[idx]])
    recur(idx + 1, chosen)

recur(0, [])



# name = ['MIN', 'CO', 'TIM']


# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return

#     # 부분집합에 포함 시키는 경우
#     recur(cnt + 1, subset + [name[cnt]])
#     # 포함 시키지 않는 경우
#     recur(cnt + 1, subset)


# recur(0, [])
    




