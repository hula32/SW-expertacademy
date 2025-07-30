############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, map 사용 시 감점

def calc_total(price_map, orders):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not orders: # 고객이 물품을 주문하지 않았을 때 0을 반환한다.
        return 0
    
    total = 0 # 가격 총 금액
    
    for ord in orders: # 고객 주문 목록 리스트에서 
        for price in price_map: 
            if price == ord: # 물품과 동일한 제품이 있다면 
                total += price_map.get(price) # 가격 총 금액에 그 물품의 가격을 합해라.

    return total

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(calc_total({'apple': 1000, 'pear': 800}, ['pear', 'apple', 'apple']))  # 2800
print(calc_total({'pen': 1200, 'note': 1500}, [])) # 0
print(calc_total({'apple': 1000, 'orange': 900, 'grape': 1200}, ['orange', 'orange'])) # 1800
#####################################################

