# 방법 1: get() 메서드 기본 사용
# price 키가 없는 경우 None 반환
for stock in stocks:
    print(stock.get('price'))

# 방법 2: get() 메서드에 기본값 설정
# price 키가 없는 경우 '비상장 주식입니다.' 반환
for stock in stocks:
    print(stock.get('price', '비상장 주식입니다.'))