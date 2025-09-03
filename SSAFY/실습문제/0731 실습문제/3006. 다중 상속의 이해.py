class BaseModel: # BaseModel 설계도 만들기 
    PK = 1 # 클래스 변수
    TYPE = 'Basic Model'

    # 클래스 변수를 사용할 때는 : 클래스명.클래스변수명
    # 인스턴스 변수를 사용할 때는
    #  - 인스턴스명.인스턴스변수명 (클래스 외부에서 쓸 때)
    #  - self.인스턴스변수명 (인스턴스 메서드 안에서 쓸 때)

    def __init__(self, data_type, title, content, created_at, updated_at): #생성자 => 새로운 인스턴스를 만든다!
        self.PK = BaseModel.PK
        # self.PK : 인스턴스 변수
        # BaseModel.PK : 클래스 변수
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1 # 클래스 변수 수정
    
    def save(self):
        print('데이터를 저장합니다.')


# author 인자를 추가로 받기
class Novel(BaseModel): # BaseModel을 상속받아서 Novel이라는 자식 클래스 생성
    def __init__(self, data_type, title, content, created_at, updated_at, author): # 자식 클래스의 생성자를 새로 정의
        super().__init__(data_type, title, content, created_at, updated_at) # 부모 클래스의 생성자 호출
        self.author = author
        
    
class Other(BaseModel): # BaseModel을 상속받아서 Other 자식클래스 생성
    TYPE = 'Other Model' # 클래스 변수를 수정

    # 만약 자식에서 생성자를 정의하지 않았다면, 부모 생성자를 가져다 씀.

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    def display_info(self):
        print(f'PK: {self.PK}, TYPE: {Other.TYPE}, Extended Type: {self.extended_type}')

    def save(self):
        print('데이터를 확장해서 저장합니다.')


# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK) # hong이라는 인스턴스가 가지고 있는 인스턴스 변수 PK
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)

print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
extended_instance = ExtendedModel('소설', '홍길동', '고전 소설','회사 설명', 1618, 1692, 'Extended Type')
extended_instance.display_info()
extended_instance.save()
