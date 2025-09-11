import heapq

arr = [20, 15, 19, 4, 13, 11]

heapq.heapify(arr)
print(arr)

min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)
print(max_heap)

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end = ' ')

arr = ['apple', 'banana', 'kiwi', 'abcd', 'abca', 'lemon', 'peach', 'grape', 'pear']

arr.sort(key=lambda x : (len(x), x))
dictionary = []

for word in arr:
    heapq.heappush(dictionary, (len(word), word))
print(dictionary)

while dictionary:
    length, word = heapq.heappop(dictionary)
    print(f'문자 길이 : {length}, 단어 : {word}')


