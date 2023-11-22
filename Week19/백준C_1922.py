import sys
sys.stdin  = open('input.txt', 'r')

# 특정 원소가 속한 집합을 찾기
# 부모 노드를 찾는 함수
def find_parent(x): # 3
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x: 
        parent[x] = find_parent(parent[x]) 
    return parent[x]

# 두 원소가 속한 집합을 합치기
# 두 부모 노드를 합치는 함수, 더 작은 값으로 부모를 갱신 시키기
def union_parent(a, b): # 
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력 받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        print(parent)
        result += cost

print(result)





# import heapq
# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]
# answer = 0

# for i in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((c,b))
#     graph[b].append((c,a))

# queue = []
# heapq.heappush(queue, (0,1))

# def Prim():
#     global answer
#     while queue:
#         wei, now = heapq.heappop(queue)
#         if visited[now] == False:
#             visited[now] = True
#             answer += wei
#             for next_wei, next_node in graph[now]:
#                 heapq.heappush(queue, (next_wei, next_node))
#     return answer

# print(Prim())