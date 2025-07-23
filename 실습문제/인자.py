def greet(name, age = 30) :
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
greet('charlie', 40)


def greet(name, age) :
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name = 'Dave', age = 35)
greet(age = 35, name = 'Dave')
# greet(age = 35, 'Dave') 오류