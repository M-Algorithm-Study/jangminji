import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque

N = int(input())
sea = []
for _ in range(N):
    graph = list(map(int, input().split()))
    sea.append(graph)

dx = [0, 0, 1, -1]
dy = [1 ,-1 ,0, 0]

# 상어 위치 찾기
for n in range(N):
    if 9 in sea[n]:
        shark_x = n
        shark_y = sea[n].index(9)
        sea[shark_x][shark_y] = 0

baby_size = 2
total_days = 0
eat = 0
while True:
    q = deque()
    # 상어 처음 위치 or 물고기를 잡아 먹을때
    q.append((shark_x, shark_y, 0))
    visited = [[False] * N for _ in range(N)]
    flag = 1e9
    fish = []

    while q:
        x, y, count = q.popleft()
        # 먹을 수 있는 물고기보다 돌고 있는 현재 위치가 더 멀 경우 반복문 종료
        if count > flag:
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 상하좌우가 범위 안에 있는 경우!!
            if 0 <= nx < N and 0 <= ny < N: 
                # 아직 방문하지 않은 경우와 물고기 크기가 아기 상어보다 작은 경우
                if visited[nx][ny] == False and sea[nx][ny] <= baby_size: 
                    # 0보다 크고 상어보다 작은 경우(즉 먹을 수 있는 물고기일 경우)
                    if 0 < sea[nx][ny] < baby_size:
                        fish.append((nx, ny, count + 1)) # fish에 자리와 움직임을 넣어주고
                        flag = count # 위치 표시를 count와 같게 한다

                    # 아직 방문하지 않은 경우와 물고기 크기가 아기 상어보다 작은 경우만
                    # 방문리스트 True로 바꾸고 q에 넣는다
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))

    # 이동 횟수가 같은 물고기 들이 여러마리면 아래 코드로
    if len(fish) > 0:
        fish.sort() 
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        # print(x, y, move)
        # print(fish)
        total_days += move
        eat += 1
        sea[x][y] = 0 # 잡아먹힘
        if eat == baby_size:
            baby_size += 1
            eat = 0
        shark_x, shark_y = x, y
    else:
        break
print(total_days)    




