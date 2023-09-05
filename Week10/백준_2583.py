import sys
sys.stdin  = open('input.txt', 'r')

M, N, K = map(int, input().split())

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

graph = []
for _ in range(M):
    graph.append([0]*N)

# 그래프 만들기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2-x1):
        for j in range(y2-y1):
            graph[y1+j][x1+i] = 1

# 전체 탐색
stack = []
result = []
for x in range(N):
    for y in range(M):
        # 그래프가 0이면
        if graph[y][x] == 0:
            cnt = 1
            graph[y][x] = 3
            stack.append((x,y))
            # while문 시작
            while stack:
                a, b = stack.pop()
                for n in range(4):
                    nx = a + dx[n]
                    ny = b + dy[n]
                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        stack.append((nx,ny))
                       
                        graph[ny][nx] = 3
                        cnt += 1
            result.append(cnt)
result.sort()
print(len(result))
print(*result)
            

