word = input().strip()
word = word.lower()

words = set()

for w in word:
    words.add(w)


cnt_num = []
for i in words:
    i.count(i)
    print(i)

print(words)
