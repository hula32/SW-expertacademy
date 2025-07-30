############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, filter 사용 시 감점
def maintenance_stats(bus_list):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not bus_list: # 버스 번호 리스트가 없을 경우 오류를 방지하기 위해 None 설정
        return (0,0)
    count = 0 # 짝수 번호 수 
    total = 0 # 짝수 번호 합계

    for bus in bus_list:
        if bus % 2 == 0: # 짝수 번호일 경우, count + 1, total + 버스 번호
            count += 1 
            total += bus

    return count, total # 튜플로 짝수 번호와 짝수 번호 합계 
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(maintenance_stats([12, 7, 10, 5, 8]))      # (3, 30)
print(maintenance_stats([3, 5, 7]))              # (0, 0)
print(maintenance_stats([2, 4, 6, 8, 10, 12]))   # (6, 42)
#####################################################