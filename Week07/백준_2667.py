import sys
sys.stdin  = open('input.txt', 'r')

N = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 2중 리스트로 그래프 받기
graph = []
for _ in range(N):
    number = input()
    number = list(map(int, number))
    graph.append(number)

result_dict = {}
stack = []
cnt = 0

# 전체 리스트 돌기
for i in range(N):
    for j in range(N):
        # 방문하지 않고 집인 경우에만
        if graph[i][j] != 0:
            # 다시 돌지 않게 0으로 만들어주고
            graph[i][j] = 0
            stack.append((i,j))
            # 각 단지에 속하는 집의 수 알기 쉽게 딕셔너리 만들기(집이 없는 경우도 있을 수 있기 때문에 처음부터 cnt를 1로 두면 안 되지 않을까...)
            result_dict[cnt+1] = 1
            while stack:
                x,y  = stack.pop()
                for n in range(4):
                    n_x = x + dx[n]
                    n_y = y + dy[n]
                    # 범위 안에 있고, 집이면
                    if 0 <= n_x < N and 0 <= n_y < N and graph[n_x][n_y] == 1:                       
                        stack.append((n_x,n_y))
                        result_dict[cnt+1] += 1   
                        # 다시 돌지 않기 위해서 0으로 만들기
                        graph[n_x][n_y] = 0                         
            cnt += 1

print(len(result_dict))
result = sorted(result_dict.values())
for r in result:
    print(r)




# max_cnt = max(map(max, graph))