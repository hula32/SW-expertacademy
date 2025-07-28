def restructure_word(word, arr):
    for w in word: # word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
        if  w.isdecimal():
            for _ in range(int(w)):
                arr.pop()
        else:
            arr.remove(w)
    return arr        

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
print(arr)
'''
결과 값

['코', '딩', ' ', '공', '부', '는', 'ㄴ', ' ', '1', '일', 'ㄹ', ' ', '1', '커', 'ㅓ', '밋',
 'ㅅ', ' ', '@', '@', '@', '#', '^', '(', ')', '#', '_', '+', '!', '&', '~', ':', '"']
'''

result = restructure_word(word, arr)
print(result)
print(''.join(result))
