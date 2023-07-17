import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque

def bfs():
    seignant = 0
    q = deque([])
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1: # 익은 토마토
                    q.append((h,i,j))
                    visited[h][i][j] = 1
                elif arr[h][i][j] == 0:
                    seignant += 1
    while q:
        qh, qi, qj = q.popleft()
        # 6방향 확인
        for move in range(6):
            nh, ni, nj = qh+dz[move], qi+dx[move], qj+dy[move]
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and visited[nh][ni][nj] == 0:
                q.append((nh,ni,nj))
                visited[nh][ni][nj] = visited[qh][qi][qj] + 1
                seignant -= 1

    if seignant == 0:
        return visited[qh][qi][qj] - 1
    else:
        return -1
M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
result = bfs()
print(result)
