T = int(input())

for t in range(1, T+1):
    N = list(input().encode('utf-8'))
    '''
    78, 108, 98, 71, 89, 103, 97, 88, 77, 103, 89, 
    83, 66, 120, 100, 87, 57, 48, 89, 88, 82, 112, 
    98, 50, 52, 117]

    '''

    arr = [0] * 64

    arr[:26] = ''.join([chr(i) for i in range(65, 91)])
    arr[26:52] = ''.join([chr(i) for i in range(97, 123)])
    arr[52:62] = ''.join([chr(i) for i in range(48, 58)])
    arr[62:] = '+', '/'

    '''
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '+', '/']
    '''
    
    for idx, N in enumerate(arr):
        
    

    # print(decoded)