# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self): # 사용자로부터 이름과 나이를 입력받는 메서드
        try:
            self.user_data['name'] = input('이름을 입력하세요 : ')
            if 'name' not in self.user_data or self.user_data['name'] == '':
                return None
            self.user_data['age'] = int(input('나이를 입력하세요 : '))
            if 'name' in self.user_data and 'age' in self.user_data:
                return True

        except Exception:
            print('나이는 숫자로 입력해야 합니다.')
            return False
            
    def display_user_info(self): # 입력된 이름과 나이를 출력하는 메서드
        try:
            name, age = self.user_data['name'], self.user_data['age']
            # name = self.user_data['name']
            # age = self.user_data['age']
            print(f'사용자 정보 : ')
            print(f'이름: {name}')
            print(f'나이: {age}')
        except Exception:
            print('사용자 정보가 입력되지 않았습니다.')
        


user = UserInfo()
user.get_user_info()
user.display_user_info()