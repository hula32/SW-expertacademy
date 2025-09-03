A = list(map(int, input().split()))

def counting_sort(data, temp, k):

    counts = [0] * 1000002

    for i in range(len(data)):
        counts[data[i]] += 1

    for i in range(1, k+1):
        counts[i] += 