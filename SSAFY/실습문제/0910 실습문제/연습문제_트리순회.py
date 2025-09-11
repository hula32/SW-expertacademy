arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

nodes = [[] for _ in range(14)]

'''
[[], [2, 3], [4], [5, 6], [7], [8, 9], [10, 11], [12], [], [], [], [13], [], []]
'''

for i in range(0, len(arr), 2):
    parent = arr[i]
    child = arr[i+1]
    nodes[parent].append(child)


for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def order(node):
    if node == None:
        return
    
    order(nodes[node][0])
    print(node, end = ' ')
    order(nodes[node][1])

order(1)

