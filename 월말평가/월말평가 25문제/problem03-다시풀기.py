# problem03.py
# ---
# 정싸피는 이번 프로젝트에서 회원가입 유효성 검사팀에 들어가게 되었다.
# 신규 아이디 생성 시 아이디와 비밀번호 모두 빈 값이 입력되는 것을 방지하고자 한다.
# 사용자의 입력 정보인 `user_data`가 python의 `dictionary` 형태로 들어온다고 할 때,
# 사용자가 입력한 아이디와 비밀번호 중 하나라도 "비어있는 문자열"이면 `False`, 그렇지 않으면 `True`를 반환하는 `is_user_data_valid` 함수를 완성하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    user_id = user_data.get('id', '')
    user_password = user_data.get('password', '')
    
    if not user_id or not user_password:
        return False
    else:
        return True





# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False

user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True

user_data3 = {
    'id': 'test_id',
    'password': '',
}
print(is_user_data_valid(user_data3)) # False

user_data4 = {
    'id': '',
    'password': '',
}
print(is_user_data_valid(user_data4)) # False