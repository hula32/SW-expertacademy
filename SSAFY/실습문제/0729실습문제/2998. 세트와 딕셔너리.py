my_set = {'가', '나', (0, 0)} # 키
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    } # 값
var = (1, 2, 3, 'A')
# 아래에 코드를 작성하시오.

for s_val in my_set:
    if my_dict.get(s_val):
        print(my_dict[s_val])
    else :
        print("None")
var1 = {var : "변수로도 키 설정 가능"}
my_dict.update(var1)
print(my_dict)


