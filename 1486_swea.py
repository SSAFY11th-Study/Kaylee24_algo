from itertools import combinations

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    minimum = float('inf')
    for i in range(1, N+1):
        case = list(combinations(height, i))
        for j in range(len(case)):
            temp = sum(case[j]) - B
            if 0 <= temp < minimum:
                minimum = temp

    print(f'#{t} {minimum}')