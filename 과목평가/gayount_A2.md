## 버블버블 해설

```python

# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    # 배열 크기 입력
    N = int(input())
    # 정수 배열 입력
    arr = list(map(int, input().split()))

    swap_count = 0  # 교환 횟수 초기화

    # 버블 정렬 수행
    for i in range(N - 1):  # 총 N-1번 패스 반복
        for j in range(N - 1 - i):  # 비교 범위 점점 줄어듦
            if arr[j] > arr[j + 1]:  # 현재 원소가 다음 원소보다 크면
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 서로 교환
                swap_count += 1  # 교환 횟수 1 증가
        # 한 패스가 끝난 후 현재 배열 상태 출력
        print(' '.join(map(str, arr)))

    # 모든 패스가 끝난 후 총 교환 횟수 출력
    print(swap_count)

```