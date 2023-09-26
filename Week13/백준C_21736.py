import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
uni = []
for _ in range(N):
    graph = list(input())
    uni.append(graph)

dx = [0, 0, 1, -1]
dy = [1 ,-1 ,0, 0]

# 도연이 위치 찾기
for n in range(N):
    if "I" in uni[n]:
        d_y = n
        d_x = uni[n].index("I")
        uni[d_y][d_x] = "X"



q = deque()
q.append((d_y,d_x))
person = 0

# 상하좌우로 이동하기
while q:
    y, x = q.popleft()
    for n in range(4):
        n_x = x + dx[n]
        n_y = y + dy[n]
        # 상하좌우가 범위 안에 있고,
        if 0 <= n_x < M and 0 <= n_y < N:
            # X가 아닌 경우
            if uni[n_y][n_x] != "X":
                # 그 중에서 P인 경우에는 변수에 +1
                if uni[n_y][n_x] == "P":
                    person += 1
                # 상하좌우 범위 안에 있고 X가 아니면 q에 담아줌 그리고 다시 돌지 않기 위해서 X로 만들어줌
                q.append((n_y, n_x))
                uni[n_y][n_x] = "X"
if person:
    print(person)
else:
    print("TT")
