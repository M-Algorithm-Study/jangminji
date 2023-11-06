from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
q = deque([N])
visited[N] = 0
cnt = 0
while q:
    cur = q.popleft()
    cnt += 1
    print("cnt", cnt, "cur", cur)
    if cur == K:
        print(visited[cur])
        break
    for i in (cur * 2, cur + 1, cur - 1):
        if 0 <= i <= 100000 and (visited[i] == -1 or visited[i] > visited[cur]):
            if i == (cur * 2):
                visited[i] = visited[cur]
                q.appendleft(i)
                
            else:
                visited[i] = visited[cur] + 1
                q.append(i)
# 왜 틀렸다고 나와요.....ㅜㅠ 해결!