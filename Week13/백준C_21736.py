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

while q:
    y, x = q.popleft()
    for n in range(4):
        n_x = x + dx[n]
        n_y = y + dy[n]
        if 0 <= n_x < M and 0 <= n_y < N:
            if uni[n_y][n_x] != "X":
                if uni[n_y][n_x] == "P":
                    person += 1
                q.append((n_y, n_x))
                uni[n_y][n_x] = "X"
if person:
    print(person)
else:
    print("TT")
