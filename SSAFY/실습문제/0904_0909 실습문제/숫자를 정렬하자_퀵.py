T = int(input())

def partition(left, right):
    pivot = number[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and number[i] <= pivot:
            i += 1
        while i <= j and number[j] >= pivot:
            j -= 1

        if i < j:
            number[i], number[j] = number[j], number[i]
    
    number[left], number[j] = number[j], number[left]

    return j


def quick_sort(left, right):
    if left < right:
        pivot = partition(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)


for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    quick_sort(0, len(number)-1)
    print(f'#{t}', *number)