import sys
sys.stdin  = open('input.txt', 'r')

import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

queue = []
heapq.heappush(queue, (0,1))

def Prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                heapq.heappush(queue, (next_wei, next_node))
    return answer

print(Prim())




























# N = int(input())
# M = int(input())
# visited = [0] * (N + 1)
# visited[0] = 1
# stack = []

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     stack.append((a, b, c))

# stack.sort(key=lambda x : (-x[2]))
# cost = 0
# while stack:
#     a, b, c = stack.pop()
    
#     if 0 not in visited:
#         print(cost)
#         break
    
#     if visited[a] == 1 and visited[b] == 1:
#         continue
#     else:
#         print(a, b, c)
#         visited[a] = 1
#         visited[b] = 1
#         cost += c


