# 오름차순 변경
def bubble_sort(a, N):
    for i in range(N-1, 0, -1): # i : 4, 3, 2, 1
        for j in range(i):
            '''
            j : 0 1 2 3
                0 1 2 
                0 1
                0
            '''
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        



# 내림차순 변경
def bubble_reverse(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]




arr = [55, 7, 78, 12, 42]
bubble_sort(arr, len(arr))
print(arr)

bubble_reverse(arr, len(arr))
print(arr)
=======
# 오름차순 변경
def bubble_sort(a, N):
    for i in range(N-1, 0, -1): # i : 4, 3, 2, 1
        for j in range(i):
            '''
            j : 0 1 2 3
                0 1 2 
                0 1
                0
            '''
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        



# 내림차순 변경
def bubble_reverse(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]




arr = [55, 7, 78, 12, 42]
bubble_sort(arr, len(arr))
print(arr)

bubble_reverse(arr, len(arr))
print(arr)
>>>>>>> 075f6b5d78fd04aa8995c922e2d2f6abf160e832
