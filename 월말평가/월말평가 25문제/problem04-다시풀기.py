# problem04.py
# ---
# 정싸피는 이번 프로젝트에서 회원가입 유효성 검사팀에 들어가게 되었다.
# 신규 생성 아이디의 마지막 글자는 반드시 0부터 9 사이의 숫자로 끝나야 한다.
# 사용자의 입력 정보인 `user_data`가 python의 `dictionary` 형태로 들어온다고 할 때,
# 사용자가 입력한 아이디가 위 조건을 만족하면 `True`, 그렇지 않으면 `False`를 반환하는 `is_id_valid` 함수를 완성하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user_data):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    user_id = user_data.get('id', '')
    if not user_id:
        return False
    
    if user_id[-1].isdigit():
        return True
    else:
        return False
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False

user_data3 = {
    'id': 'test0',
    'password': 'abc',
}
print(is_id_valid(user_data3)) # True

user_data4 = {
    'id': 'test', # 숫자로 끝나지 않음
    'password': 'abc',
}
print(is_id_valid(user_data4)) # False

user_data5 = {
    'id': '', # 빈 문자열
    'password': 'abc',
}
print(is_id_valid(user_data5)) # False