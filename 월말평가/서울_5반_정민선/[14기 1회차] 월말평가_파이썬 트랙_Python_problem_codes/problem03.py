############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, len, filter, 리스트 count 메서드 사용 시 감점
def defect_rate(results):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    total = 0.0 # pass(0)와 fail(1)의 값의 합계 / float로 표현하기 위해 0.0으로 초기 값 설정
    count = 0 # 인자의 개수

    for str in results:
        if str == 'pass': # pass인 경우 0, 인자의 개수 +1
            total += 0
            count += 1
        elif str == 'fail': # fail인 경우 1, 인자의 개수 +1
            total += 1
            count += 1
    
    return total / count # 합계와 인자의 개수를 나눠 불량률 도출

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(defect_rate(['pass', 'fail', 'pass', 'fail']))   # 0.5
print(defect_rate(['pass', 'pass']))                   # 0.0
print(defect_rate(['fail', 'fail', 'fail']))           # 1.0
#####################################################