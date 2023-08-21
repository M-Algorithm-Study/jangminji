import sys
sys.stdin  = open('input.txt', 'r')
from collections import deque

N, K = map(int,input().split())
visited = [0] * 100001

stack = deque()
stack.append(N)
cnt = 0
while stack:
    cur = stack.popleft()
    cnt += 1
    if cur == K:
        # print(stack)
        print(visited[cur], cnt)
        break
    
    for i in (cur+1, cur-1, 2*cur):
        if 0<= i <= 100000 and visited[i] == 0:
            stack.append(i)
            visited[i] = visited[cur] + 1

# cur = 5, i = 6, 4, 10
# stack = [6, 4, 10]
# visited[6,4,10] = visited[5] + 1 = 0 + 1






