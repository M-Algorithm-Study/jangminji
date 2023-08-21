from collections import deque

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = 0

while True:
    # 새로운 날
    stack = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    stack.append([0, 0])

    # 공기를 while문으로 연결된 부분 전체 탐색 (자동으로 stack에 담기지 않음 )
    while stack:
        x, y = stack.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 안에 있는 경우 중에서
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 치즈인 경우와
                if cheeze[nx][ny] != 0:
                    cheeze[nx][ny] += 1
                # 공기인 경우에만 다시 방문하지 않기 위해 방문리스트에 표시해주고, 사방으로 돌기 위해서 stack에 넣어준다.
                else:
                    visited[nx][ny] = 1
                    stack.append([nx, ny])

    # 상한 치즈 확인하는 코드
    check = 0
    for i in range(N):
        for j in range(M):
            # 2개의 면적이 공기 중에 닿아서 +2가 된 경우 3이 된다.
            # 이 경우엔 치즈를 0으로 초기화 시켜준다.
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
            
            # 1인 경우나 2인 경우일 경우 (외부와 닿는 면적이 2개 미만인 치즈들)
            elif 2 == cheeze[i][j] or 1 == cheeze[i][j]:
                check = 1
                cheeze[i][j] = 1
    days += 1

    # 상한 치즈를 확인하는 부분에서 치즈인 경우는 flag가 1이 변하는데 변하지 않는 경우는 while문 종료
    if check == 0:
        print(days)
        break