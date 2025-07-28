# 아래 함수를 수정하시오.
def reverse_string(str):
    r_str = "".join(reversed(str))
    # 리스트를 문자열로 변환할 때 자주 쓰임 "".join

    return r_str


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH