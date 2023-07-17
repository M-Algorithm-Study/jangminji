import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N * H)]
new_graph = [row for row in graph]
visited = [[0] * M for _ in range(N * H)]



dx = [-1, 1, 0, 0, -N, N]
dy = [0, 0, -1, 1, 0, 0]
# print(dx, dy)

def ripen_tomatoes(graph, visited, M, N, H):
    seignant = 0
    q = deque([])
    days = 0
    for i in range(N * H):
        for j in range(M):
            if graph[i][j] == 1:
                q.append([i,j])
                visited[i][j] = 1
            elif graph[i][j] == 0:
                seignant += 1
    # print(new_graph)
    while q:
        qi, qj = q.popleft()  

        for move in range(6):
            new_x = qi + dx[move]
            new_y = qj + dy[move]
            
            if 0 <= new_x < N*H and 0 <= new_y < M and graph[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                q.append([new_x, new_y])
                seignant -= 1
                visited[new_x][new_y] = visited[qi][qj] + 1
               
    if seignant == 0:
        return visited[qi][qj] - 1
    else:
        return -1


result = ripen_tomatoes(graph, visited, M, N, H)
print(result)

# M, N, H = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(N * H)]
# new_graph = [row for row in graph]
# visited = [[False] * M for _ in range(N * H)]



# dx = [-1, 1, 0, 0, -N, N]
# dy = [0, 0, -1, 1, 0, 0]
# # print(dx, dy)

# def ripen_tomatoes(graph, visited, M, N, H):
#     seignant = 0
#     for g in graph:
#         seignant += g.count(0)
#     print(seignant)
#     new_graph = [[0] * M for _ in range(N * H)]
#     days = 0
#     # print(new_graph)
#     while True:
#         ripe_tomatoes = True
#         for i in range(N * H):
#             for j in range(M):
#                 if new_graph[i][j] == 1:
#                     graph[i][j] = new_graph[i][j]

#                 new_graph[i][j] = graph[i][j]
#         for i in range(N * H):
#             for j in range(M):
                
#                 if not visited[i][j] and graph[i][j] == 1:
#                     # print("ij",i,j)
#                     ripe_tomatoes = False
#                     visited[i][j] = True

#                     for move in range(6):
#                         new_x = i + dx[move]
#                         new_y = j + dy[move]
                       
#                         if 0 <= new_x < N*H and 0 <= new_y < M and graph[new_x][new_y] == 0:
#                             print("ㅁ",graph)
#                             new_graph[new_x][new_y] = 1
#                             seignant -= 1
#                             print(seignant)
#                             # print(new_graph)
                            
#                             print("new",new_x, new_y)
#                             print("n",new_graph)
            
#         if ripe_tomatoes:
#             if seignant == 0:
#                 print("return",graph)
#                 return days - 1
#             else:
#                 # print("seg", seignant)
#                 return -1

        
        
#         # graph = [row for row in new_graph]
    
#         for i in range(N * H):
#             for j in range(M):
#                 if new_graph[i][j] == 1:
#                     graph[i][j] = new_graph[i][j]
#         days += 1

# result = ripen_tomatoes(graph, visited, M, N, H)
# print(result)